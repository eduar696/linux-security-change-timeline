# linux-security-change-timeline 🛡️

## 🚀 Sobre el proyecto
En ciberseguridad, **si no se registró, no ocurrió**. Los cambios pequeños en la configuración de un servidor Linux a menudo pasan desapercibidos, creando brechas de seguridad o configuraciones erróneas que permanecen ocultas hasta que ocurre un incidente. 

Esta herramienta automatiza la **auditoría de integridad (FIM)**, permitiendo a los administradores y analistas de seguridad mantener una línea de tiempo (timeline) precisa de los cambios críticos en sistemas Linux.

## 👁️ Visualización del Reporte
![Auditoría de Cambios](screenshots/auditoria_deteccion_cambio.png)

## ✨ Capacidades de Detección
La herramienta realiza una comparación inteligente entre instantáneas del sistema, detectando modificaciones en:

- ✔ **Gestión de Identidad:** Cambios en `/etc/passwd` y `/etc/group` (nuevos usuarios/grupos).
- ✔ **Hardening SSH:** Modificaciones en `sshd_config` que podrían comprometer el acceso remoto.
- ✔ **Control de Red:** Cambios en reglas de firewall (`iptables`/`ufw`).
- ✔ **Servicios del Sistema:** Auditoría del estado y configuración de servicios activos.
- ✔ **Archivos Sensibles:** Monitoreo de integridad en archivos con permisos elevados.

## 📊 Resultado
El sistema genera un reporte de auditoría estructurado en Markdown, permitiendo identificar en segundos:
1. **Qué cambió:** (Diferencias exactas con formato diff).
2. **Cuándo cambió:** (Basado en el timestamp de la captura).
3. **Impacto:** (Severidad del cambio detectado).

## 🏗️ Arquitectura
El flujo de trabajo está diseñado para ser ligero y eficiente:
`Servidor Linux` → `Recolección` → `Análisis Forense` → `Timeline Report`.
*Consulta la [documentación detallada aquí](docs/architecture.md).*

## 📁 Estructura del Proyecto
- `docs/`: Diagramas de arquitectura y documentación técnica.
- `evidence/`: Repositorio de instantáneas (snapshots) históricas.
- `scripts/`: Motor de automatización (Python).
- `timeline/`: Informes de auditoría generados listos para revisar.
- `screenshots/`: Evidencia visual de la herramienta funcionando.
