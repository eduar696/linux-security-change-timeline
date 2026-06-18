# Arquitectura del Sistema

El sistema sigue un flujo de trabajo lineal diseñado para garantizar la integridad y trazabilidad de los datos:

### Diagrama de Flujo
```text
[ Servidor Linux ] 
       |
       v
[ Script de Recolección (collect_evidence.py) ] --> (Guarda snapshot en /evidence)
       |
       v
[ Script de Análisis (build_timeline.py) ] <--- (Compara /evidence)
       |
       v
[ Reporte de Trazabilidad (timeline.md) ]
