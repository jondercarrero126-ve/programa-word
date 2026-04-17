# Tasks: Fase 2 - Exportar y Gráficos

## Phase 1: Infrastructure (5 tasks)
| # | Task | File | Verification |
|---|------|------|--------------|
| 1.1 | Add tesis_por_anio, tesis_por_estado, tesis_por_autor queries | database/__init__.py | Query returns correct aggregation |
| 1.2 | Add get_tesis_by_id(id) to TesisController | principal.py | Returns complete thesis dict |
| 1.3 | Add obtener_datos_graficos() to TesisController | principal.py | Returns dict with 3 chart datasets |
| 1.4 | Add export method signatures to TesisController | principal.py | Methods accept thesis_id, output_path |
| 1.5 | Verify matplotlib and reportlab installed | requirements/env | pip list shows packages |

## Phase 2: Core Implementation (6 tasks)
| # | Task | File | Verification |
|---|------|------|--------------|
| 2.1 | Create word_exporter/__init__.py with WordExporter class | word_exporter/__init__.py | Class instantiates without error |
| 2.2 | Implement set_title, set_author, set_abstract, set_keywords | word_exporter/__init__.py | Document properties set correctly |
| 2.3 | Implement add_chapter, add_reference, save methods | word_exporter/__init__.py | .docx file created and readable |
| 2.4 | Create pdf_exporter/__init__.py with PdfExporter | pdf_exporter/__init__.py | Class instantiates without error |
| 2.5 | Implement PDF export using docx2pdf or reportlab | pdf_exporter/__init__.py | .pdf file created from docx |
| 2.6 | Create matplotlib chart widgets for Análisis | principal.py | Bar/pie charts render in widget |

## Phase 3: Integration (6 tasks)
| # | Task | File | Verification |
|---|------|------|--------------|
| 3.1 | Add "Exportar Word" button to Panel in principal.py | principal.py | Button visible and enabled |
| 3.2 | Add "Exportar PDF" button to Panel in principal.py | principal.py | Button visible and enabled |
| 3.3 | Add chart widgets (bar, pie) to Análisis page | UI/principal.ui + ui_principal.py | Charts display data |
| 3.4 | Create ExportWorker(QThread) with finished/error signals | principal.py | Thread runs without blocking UI |
| 3.5 | Connect export buttons to ExportWorker slots | principal.py | Click triggers worker execution |
| 3.6 | Connect Análisis page load to _actualizar_graficos() | principal.py | Charts refresh on page visit |

## Phase 4: Testing (4 tasks)
| # | Task | File | Verification |
|---|------|------|--------------|
| 4.1 | Unit test WordExporter core methods | tests/test_word_exporter.py | 8+ tests pass |
| 4.2 | Unit test obtener_datos_graficos() | tests/test_tesis_controller.py | Returns correct datasets |
| 4.3 | Integration test ExportWorker signals | tests/test_gui.py | qtbot.waitSignal passes |
| 4.4 | E2E test full export flow (manual) | scripts/test_export.py | Word+PDF files match input |

---

## Implementation Order
1. Phase 1 first (database + controller foundations)
2. Phase 2 second (exporters + chart logic)
3. Phase 3 third (UI integration + threading)
4. Phase 4 last (verify everything works)

## Dependencies
- Phase 1 → Phase 2 (controllers ready before exporters use them)
- Phase 2 → Phase 3 (exporters ready before UI connects)
- Phase 1+2+3 → Phase 4 (full system tested together)

## Open Questions (for later)
- PDF: docx2pdf (requires Word installed) vs reportlab (independent)?
- Chart types priority: bar (año), pie (estado), line (trend)?
- Export UI: toolbar buttons or context menu?