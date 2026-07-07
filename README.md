# Linux-Security-Change-Timeline 🛡️

## 🚀 Sobre el proyecto

En ciberseguridad, **si no se registró, no ocurrió**.

Los cambios en la configuración de un servidor Linux pueden pasar desapercibidos durante días o semanas, dificultando la investigación de incidentes y la identificación del momento exacto en que una configuración crítica fue modificada.

**Linux-Security-Change-Timeline** es un proyecto personal desarrollado en Python que automatiza la recolección de instantáneas (snapshots) de configuraciones críticas de un sistema Linux y genera una línea de tiempo con las diferencias detectadas entre capturas.

El objetivo del proyecto es demostrar conocimientos de automatización, administración de Linux y auditoría básica de configuraciones mediante reportes fáciles de interpretar.

---

# 🏗️ Problema y Solución

### Problema

Durante una investigación forense o una revisión de seguridad suele ser difícil responder preguntas como:

- ¿Qué cambió?
- ¿Cuándo ocurrió el cambio?
- ¿Qué archivo fue modificado?

Aunque Linux dispone de distintas herramientas de auditoría, muchas generan grandes volúmenes de información o requieren configuraciones más avanzadas.

### Solución

Este proyecto realiza capturas periódicas de configuraciones críticas del sistema y compara cada snapshot con el anterior para generar un reporte en formato Markdown que muestra las diferencias encontradas mediante un formato tipo **diff**.

No pretende reemplazar herramientas especializadas de monitoreo continuo, sino ofrecer una forma sencilla de visualizar cambios históricos en configuraciones relevantes.

---

# 👁️ Visualización del Reporte

![Auditoría de Cambios](screenshots/auditoria_deteccion_cambio.png)

El reporte permite visualizar de forma sencilla las diferencias entre dos snapshots consecutivos, facilitando la revisión manual de cambios realizados en archivos sensibles.

---

# ✨ Capacidades de Detección

Actualmente el proyecto analiza cambios en configuraciones relacionadas con:

- ✔ Gestión de usuarios (`/etc/passwd` y `/etc/group`)
- ✔ Configuración de SSH (`sshd_config`)
- ✔ Reglas de firewall (`iptables` / `ufw`)
- ✔ Estado y configuración básica de servicios
- ✔ Archivos sensibles definidos durante la recolección

Las detecciones se basan en la comparación entre snapshots consecutivos del sistema.

---

# 📊 Resultado

El proyecto genera un reporte de auditoría en Markdown donde se pueden identificar:

1. Qué archivo cambió.
2. Las diferencias exactas mediante formato diff.
3. Entre qué snapshots ocurrió el cambio.
4. El momento en que fue detectado.

Este reporte está pensado como apoyo para revisiones de configuración y ejercicios de auditoría en entornos Linux.

---

# 📁 Estructura del Proyecto

```
docs/
├── Documentación técnica
├── Arquitectura

evidence/
├── Snapshots recolectados

scripts/
├── Recolección
├── Comparación
├── Generación de reportes

timeline/
├── Reportes generados

screenshots/
├── Evidencia visual
```

---

# ⚙️ Arquitectura

El flujo de trabajo es simple y está orientado a facilitar la auditoría de configuraciones.

```
Servidor Linux
        │
        ▼
 Recolección de snapshots
        │
        ▼
 Comparación entre capturas
        │
        ▼
 Generación de reporte Markdown
```

El proyecto prioriza la simplicidad y la claridad del proceso sobre la implementación de una plataforma completa de monitoreo.

---

## 🎯 Objetivo del proyecto

Este repositorio fue desarrollado como proyecto de aprendizaje para practicar:

- Automatización con Python
- Administración de sistemas Linux
- Comparación de configuraciones
- Generación automática de reportes
- Organización de proyectos técnicos en GitHub

No pretende sustituir soluciones como AIDE, auditd o Wazuh, sino demostrar una implementación propia de un flujo básico de auditoría basado en snapshots.
