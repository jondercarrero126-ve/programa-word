import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="session")
def qapp_args():
    return []


def pytest_configure(config):
    config.addinivalue_line("markers", "gui: GUI tests that require Qt application")


@pytest.fixture(scope="session")
def app():
    from PySide6.QtWidgets import QApplication

    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.quit()
