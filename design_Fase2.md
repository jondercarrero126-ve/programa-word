# Design: Fase 2 - Exportar y Gráficos

## Technical Approach

Reverse the existing WordExtractor pattern to create a Word exporter. For PDF, use docx2pdf or reportlab. For charts, integrate matplotlib FigureCanvasQTAgg into the Análisis panel. All export operations run on QThread to avoid blocking the UI.

## Architecture Decisions

### Decision: Word Export Library

**Choice**: python-docx (already installed)
**Alternatives considered**: docxtpl (template-based), textX (simpler but less control)
**Rationale**: Inverse of WordExtractor - same library ensures compatibility with reverse parsing. python-docx provides full control over document structure.

### Decision: PDF Export Library

**Choice**: python-docx + docx2pdf (via pywinddle) or reportlab
**Alternatives considered**: WeasyPrint (HTML-to-PDF), fpdf (simpler but less features)
**Rationale**: If docx2pdf available, reuse Word structure. Otherwise reportlab mirrors python-docx API. Simpler than HTML conversion.

### Decision: Chart Library

**Choice**: matplotlib with FigureCanvasQTAgg
**Alternatives considered**: pyqtgraph (faster but less customizable), QtCharts (limited chart types)
**Rationale**: Industry standard, integrates directly with Qt, supports bar/pie/line charts needed for Análisis panel.

### Decision: Threading Strategy

**Choice**: QThread workers (same pattern as ImportWorker)
**Alternatives considered**: asyncio (not needed for sync I/O), concurrent.futures (less Qt integration)
**Rationale**: Consistency with existing codebase. Export is I/O-bound, not CPU-bound, but QThread provides proper signal/slot integration.

## Data Flow

```
User clicks Export → ExportWorker(QThread) → WordExporter/Database → File saved
                                                          ↓
                                              Signal → UI slot → QFileDialog.showSaveAs()
```

```
Análisis page load → _actualizar_analisis() → Database queries → Matplotlib figure → Canvas.draw()
```

## File Changes

| File | Action | Description |
|------|--------|-------------|
| `word_exporter/__init__.py` | Create | WordExporter class (inverse of WordExtractor) |
| `word_exporter/pdf_exporter.py` | Create | PDF export using docx2pdf or reportlab |
| `principal.py` | Modify | Add export buttons to Panel, chart widgets to Análisis |
| `TesisController` | Modify | Add export methods get_tesis_by_id(), obtener_datos_graficos() |
| `UI/principal.ui` | Modify | Add chart widget placeholder, export buttons |
| `UI/ui_principal.py` | Regenerate | After UI change |

## Interfaces / Contracts

```python
# WordExporter (inverse of WordExtractor)
class WordExporter:
    def __init__(self, filepath):
        self.doc = Document(filepath)
    
    def set_title(self, title)
    def set_author(self, author)
    def set_abstract(self, abstract)
    def set_keywords(self, keywords)
    def add_chapter(self, title, content)
    def add_reference(self, tipo, autor, titulo, anio, url)
    def save()

# TesisController additions
def obtener_datos_graficos(self) -> dict:
    """Returns: { tesis_por_anio, tesis_por_estado, tesis_por_autor }"""

# ExportWorker
class ExportWorker(QThread):
    finished = Signal(str)  # filepath
    error = Signal(str)
```

## Testing Strategy

| Layer | What to Test | Approach |
|-------|-------------|----------|
| Unit | WordExporter.set_* methods | Mock Document, verify calls |
| Unit | TesisController.obtener_datos_graficos | Fixture DB with test data |
| Integration | ExportWorker thread | qtbot.waitSignal |
| Integration | Chart renders | Compare pixmaps |
| E2E | Full export flow | Manual with test thesis |

## Migration / Rollout

No migration required. New functionality adds to existing structure.

## Open Questions

- [ ] Should PDF export use docx2pdf (simpler, requires Word) or reportlab (independent)?
- [ ] Which chart types prioritize: bar (tesis por año), pie (estado), line (trend)?
- [ ] Export buttons location: Panel toolbar or thesis context menu?