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
