# Skill Registry

**Delegator use only.** Any agent that launches sub-agents reads this registry to resolve compact rules, then injects them directly into sub-agent prompts. Sub-agents do NOT read this registry or individual SKILL.md files.

See `_shared/skill-resolver.md` for the full resolution protocol.

## User Skills

| Trigger | Skill | Path |
|---------|-------|------|
| PyQt6 desktop GUI development | pyqt6-ui-development-rules | C:\Users\User\Desktop\Jonder\Proyecto python\.agents\skills\pyqt6-ui-development-rules\SKILL.md |

## Compact Rules

Pre-digested rules per skill. Delegators copy matching blocks into sub-agent prompts as `## Project Standards (auto-resolved)`.

### pyqt6-ui-development-rules
- ALWAYS use Qt's signal/slot mechanism for UI-to-logic communication — never call business logic directly from UI slots
- NEVER perform long-running operations on the main UI thread — use QThread, QRunnable, or asyncio with qasync
- ALWAYS apply QSS stylesheets at QApplication level, not per-widget — use object names/classes for theming
- NEVER use absolute pixel coordinates — use layout managers (QVBoxLayout, QHBoxLayout, QGridLayout) for DPI-aware rendering
- ALWAYS test UI on all target platforms before release — rendering differs between Windows/macOS/Linux

## Project Conventions

| File | Path | Notes |
|------|------|-------|
| AGENTS.md | C:\Users\User\Desktop\Jonder\Proyecto python\AGENTS.md | Index — references files below |

| Referenced File | Path | Notes |
|-----------------|------|-------|
| main.py | C:\Users\User\Desktop\Jonder\Proyecto python\main.py | Application entry point |
| login.py | C:\Users\User\Desktop\Jonder\Proyecto python\login.py | Login window |
| principal.py | C:\Users\User\Desktop\Jonder\Proyecto python\principal.py | Main window class |
| database/__init__.py | C:\Users\User\Desktop\Jonder\Proyecto python\database\__init__.py | MySQL connection wrapper |
| word_extractor/extractor.py | C:\Users\User\Desktop\Jonder\Proyecto python\word_extractor\extractor.py | Word document parser |
| UI/principal.ui | C:\Users\User\Desktop\Jonder\Proyecto python\UI\principal.ui | Main window UI definition |
| UI/login.ui | C:\Users\User\Desktop\Jonder\Proyecto python\UI\login.ui | Login UI definition |
| UI/ui_principal.py | C:\Users\User\Desktop\Jonder\Proyecto python\UI\ui_principal.py | Generated — DO NOT EDIT |
| UI/ui_login.py | C:\Users\User\Desktop\Jonder\Proyecto python\UI\ui_login.py | Generated — DO NOT EDIT |
| tests/test_database.py | C:\Users\User\Desktop\Jonder\Proyecto python\tests\test_database.py | Database tests (14 tests) |
| tests/test_extractor.py | C:\Users\User\Desktop\Jonder\Proyecto python\tests\test_extractor.py | WordExtractor tests (12 tests) |
| tests/test_gui.py | C:\Users\User\Desktop\Jonder\Proyecto python\tests\test_gui.py | GUI tests (21 tests) |
| scripts/init_database.py | C:\Users\User\Desktop\Jonder\Proyecto python\scripts\init_database.py | Database initialization |
