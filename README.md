# Linux-Security-Change-Timeline 🛡️

## 🚀 Sobre el proyecto
En ciberseguridad, **si no se registró, no ocurrió**. Los cambios sutiles en la configuración de un servidor Linux suelen pasar desapercibidos, creando brechas de seguridad o configuraciones erróneas que permanecen ocultas hasta que ocurre un incidente.

**Linux-Security-Change-Timeline** automatiza la auditoría de integridad (FIM) y el registro histórico, permitiendo a administradores y analistas de seguridad mantener una línea de tiempo precisa de cambios críticos en sistemas Linux.

---

## 🏗️ Problema y Solución
* **Problema:** La falta de un registro histórico detallado de cambios en la configuración dificulta la auditoría forense y la detección temprana de intrusiones.
* **Solución:** Nuestra herramienta automatiza la comparación inteligente entre instantáneas (snapshots) del sistema, generando reportes estructurados que detallan **qué** cambió, **cuándo** y cuál es el **impacto** de seguridad.

---

## 👁️ Visualización del Reporte
![Auditoría de Cambios](screenshots/auditoria_deteccion_cambio.png)

## ✨ Capacidades de Detección
El motor de análisis monitorea áreas críticas para detectar cualquier modificación no autorizada:

- ✔ **Gestión de Identidad:** Cambios en `/etc/passwd` y `/etc/group` (nuevos usuarios/grupos).
- ✔ **Hardening SSH:** Modificaciones en `sshd_config` que podrían comprometer el acceso remoto.
- ✔ **Control de Red:** Cambios en reglas de firewall (`iptables`/`ufw`).
- ✔ **Servicios del Sistema:** Auditoría del estado y configuración de servicios activos.
- ✔ **Archivos Sensibles:** Monitoreo de integridad en archivos con permisos elevados.

---

## 📊 Resultado
El sistema genera un reporte de auditoría estructurado en Markdown, facilitando la investigación rápida y permitiendo identificar:
1. **Qué cambió:** Diferencias exactas con formato diff.
2. **Cuándo cambió:** Basado en el timestamp de la captura.
3. **Impacto:** Severidad del cambio detectado.

---

## 📁 Estructura del Proyecto
* `/docs`: Diagramas de arquitectura y documentación técnica detallada.
* `/evidence`: Repositorio de instantáneas (snapshots) históricas.
* `/scripts`: Motor de automatización en Python (recolección y análisis).
* `/timeline`: Informes de auditoría generados listos para revisar.
* `/screenshots`: Evidencia visual de la herramienta funcionando.

---

## ⚙️ Arquitectura
El flujo de trabajo está diseñado para ser ligero, eficiente y auditable:
`Servidor Linux` → `Recolección` → `Análisis Forense` → `Timeline Report`.

*Consulta la [documentación detallada aquí](docs/architecture.md).*
