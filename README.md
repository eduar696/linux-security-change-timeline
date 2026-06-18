# linux-security-change-timeline

## Problema
Los pequeños cambios en la configuración de un servidor Linux a menudo pasan desapercibidos, creando brechas de seguridad o configuraciones erróneas que no se detectan hasta que ocurre un incidente. La falta de un registro histórico de cambios dificulta la auditoría y la respuesta a incidentes.

## Solución
Esta herramienta automatiza la creación de una línea de tiempo (timeline) de cambios críticos de seguridad en sistemas Linux. Al comparar "instantáneas" (snapshots) del sistema, genera reportes claros que facilitan la auditoría forense y el monitoreo de integridad.

## Capacidades de Detección
- ✔ **Usuarios y Grupos:** Cambios en `/etc/passwd` y `/etc/group`.
- ✔ **Configuración SSH:** Modificaciones en `sshd_config`.
- ✔ **Firewall:** Reglas de red (`iptables`/`ufw`).
- ✔ **Servicios:** Estado y configuración de servicios críticos.
- ✔ **Archivos sensibles:** Auditoría de archivos con permisos elevados.

## Resultado
Genera un reporte de auditoría estructurado en Markdown, facilitando la investigación rápida de qué cambió, cuándo cambió y qué impacto tuvo.

## Estructura del Proyecto
- `evidence/`: Almacenamiento de las instantáneas (snapshots) del sistema.
- `scripts/`: Lógica de recolección y análisis forense.
- `timeline/`: Reportes de auditoría generados.
- `docs/`: Documentación técnica y de arquitectura.

