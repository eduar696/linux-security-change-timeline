# Arquitectura del Sistema

El proyecto sigue un flujo de trabajo sencillo basado en la recolección periódica de snapshots y su posterior compración para identificar cambios en configuraciones relevantes del sistema.

### Diagrama de Flujo
```text
[ Servidor Linux ]
       |
       v
[ collect_evidence.py ]
       |
       v
(Guarda snapshots en /evidence)
       |
       v
[ build_timeline.py ]
       |
       v
(Compara snapshots)
       |
       v
[ timeline.md ]
