"""
ThemeManager - Singleton para gestión de temas claro/oscuro en la aplicación.

Proveer cambio de tema dinámico con persistencia en config.json.
"""

import json
import os
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QApplication


class ThemeManager(QObject):
    """Singleton para gestionar temas de la aplicación.

    Uso:
        theme_manager = ThemeManager.get_instance()
        theme_manager.apply_theme()
        theme_manager.toggle_theme()
    """

    theme_changed = Signal(str)

    _instance = None

    def __init__(self):
        super().__init__()
        self._current_theme = "light"
        self._config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "config.json"
        )

    @classmethod
    def get_instance(cls):
        """Obtiene la instancia singleton del ThemeManager."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def load_preference(self):
        """Carga la preferencia de tema desde config.json.

        Returns:
            str: "light" o "dark"
        """
        try:
            if os.path.exists(self._config_path):
                with open(self._config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                    self._current_theme = config.get("theme", "light")
            else:
                self._current_theme = "light"
        except (json.JSONDecodeError, IOError):
            self._current_theme = "light"

        return self._current_theme

    def save_preference(self):
        """Guarda la preferencia de tema actual en config.json."""
        try:
            config = {}
            if os.path.exists(self._config_path):
                with open(self._config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)

            config["theme"] = self._current_theme

            with open(self._config_path, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2)
        except (json.JSONDecodeError, IOError):
            pass

    def apply_theme(self, theme_name: str = None):
        """Aplica el tema especificado a la aplicación.

        Args:
            theme_name: "light" o "dark". Si es None, usa el tema actual.
        """
        if theme_name is not None:
            self._current_theme = theme_name

        app = QApplication.instance()
        if app is None:
            return

        theme_file = os.path.join(
            os.path.dirname(__file__), f"{self._current_theme}.qss"
        )

        try:
            if os.path.exists(theme_file):
                with open(theme_file, "r", encoding="utf-8") as f:
                    qss = f.read()
                app.setStyleSheet(qss)
                self.theme_changed.emit(self._current_theme)
        except IOError:
            pass

    def toggle_theme(self):
        """Alterna entre tema claro y oscuro."""
        if self._current_theme == "light":
            self._current_theme = "dark"
        else:
            self._current_theme = "light"

        self.save_preference()
        self.apply_theme()

    def get_current_theme(self) -> str:
        """Obtiene el tema actual.

        Returns:
            str: "light" o "dark"
        """
        return self._current_theme


def get_theme_manager() -> ThemeManager:
    """Función de convenience para obtener ThemeManager.

    Returns:
        ThemeManager: Instancia singleton
    """
    return ThemeManager.get_instance()
