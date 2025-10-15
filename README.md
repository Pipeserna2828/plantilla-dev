# Performance Analyzer AI

API que recibe archivos de resultados de performance (K6 JSON o JMeter CSV), valida, genera un **summary** unificado y produce un **informe ejecutivo** con IA (stub Azure).

## Ejecutar en local
```bash
poetry install
poetry run uvicorn src.api.app:app --reload
