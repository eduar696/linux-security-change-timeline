# Linux-Security-Change-Timeline 🛡️

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-FCC624?logo=linux&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Security](https://img.shields.io/badge/Focus-Linux%20Security-darkred)
![Made With](https://img.shields.io/badge/Made%20with-Python-blueviolet)

---

## 🚀 Sobre el proyecto

En ciberseguridad, **si no se registró, no ocurrió**.

Los cambios en la configuración de un servidor Linux pueden pasar desapercibidos durante días o semanas, dificultando la investigación de incidentes y la identificación del momento exacto en que una configuración crítica fue modificada.

**Linux-Security-Change-Timeline** es un proyecto personal desarrollado en Python que automatiza la recolección de snapshots de configuraciones críticas de un sistema Linux y genera una línea de tiempo con las diferencias detectadas entre capturas consecutivas.

El objetivo del proyecto es demostrar conocimientos de automatización con Python, administración de sistemas Linux y generación de reportes de auditoría mediante un flujo sencillo y fácil de interpretar.

---

# 🏗️ Problema y Solución

### Problema

Durante una investigación forense o una revisión de seguridad suele ser difícil responder preguntas como:

- ¿Qué cambió?
- ¿Cuándo ocurrió el cambio?
- ¿Qué archivo fue modificado, añadido o eliminado?

Aunque Linux dispone de distintas herramientas para auditoría y monitoreo, muchas requieren una configuración más compleja o generan grandes volúmenes de información para escenarios donde únicamente se necesita registrar cambios de configuración.

### Solución

El proyecto realiza capturas periódicas (snapshots) de configuraciones críticas del sistema y compara cada captura con la anterior para generar un reporte en formato Markdown que muestra las diferencias encontradas mediante un formato **diff**.

Además de detectar modificaciones en archivos existentes, identifica archivos **añadidos** y **eliminados** entre snapshots, proporcionando una visión completa de la evolución de la configuración.

Su objetivo es facilitar la revisión histórica de cambios en archivos de configuración, sin sustituir herramientas especializadas de monitoreo continuo o detección de intrusiones.

---

# 👁️ Visualización del Reporte

![Auditoría de Cambios](screenshots/auditoria_deteccion_cambio.png)

El reporte permite visualizar de forma sencilla las diferencias entre dos snapshots consecutivos, facilitando la revisión manual de cambios realizados en archivos sensibles.

---

# ✨ Capacidades de Detección

Actualmente el proyecto compara snapshots para identificar:

- ✔ **Archivos modificados**: Cambios en líneas de configuraciones existentes (`/etc/passwd`, `/etc/ssh/sshd_config`, `/etc/ufw/user.rules`)
- ✔ **Archivos añadidos**: Nuevos archivos de configuración detectados en snapshots recientes
- ✔ **Archivos eliminados**: Archivos que dejaron de estar presentes entre capturas
- ✔ **Gestión de permisos**: Restauración de propiedad al usuario que ejecutó el script (cuando se usa `sudo`)

Las detecciones se basan en la comparación entre snapshots consecutivos almacenados durante la ejecución del proyecto.

---

# 📊 Resultado

El proyecto genera un reporte de auditoría en formato Markdown donde es posible identificar:

1. El archivo que fue modificado, añadido o eliminado.
2. Las diferencias encontradas mediante formato **diff**.
3. Entre qué snapshots se detectó el cambio.
4. La fecha de la comparación realizada.

El reporte está pensado como apoyo para revisiones de configuración y ejercicios de auditoría en sistemas Linux.

---

# 🛠️ Tecnologías utilizadas

- Python 3
- Linux
- Bash
- Markdown
- `os`, `shutil`, `pwd` (recolección de snapshots)
- `difflib` (comparación de archivos)
- `datetime` (timestamps)

---

# 📁 Estructura del Proyecto

```text
.
├── docs/
│   └── architecture.md          # Arquitectura y flujo del proyecto
│
├── evidence/
│   └── .gitkeep                   # Carpeta para snapshots generados localmente
│
├── scripts/
│   ├── collect_evidence.py      # Recolección de snapshots con timestamp
│   └── build_timeline.py        # Comparación, detección de cambios y generación del reporte
│
├── timeline/
│   ├── security_change_report.md
│   └── timeline.md                # Reporte generado automáticamente con diff
│
├── screenshots/
│   └── auditoria_deteccion_cambio.png
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt

```

# ⚙️ Arquitectura
El flujo de trabajo es sencillo y está orientado a facilitar la auditoría de configuraciones mediante la comparación de snapshots.


Servidor Linux
        │
        ▼
collect_evidence.py
        │
        ▼
Almacenamiento de snapshots en evidence/
        │
        ▼
build_timeline.py
        │
        ▼
Comparación entre snapshots (modificados, añadidos, eliminados)
        │
        ▼
Generación de reporte Markdown (timeline.md)

Para una descripción más detallada del flujo de trabajo, consulta docs/architecture.md.


# 🎯 Objetivo del Proyecto
Este repositorio fue desarrollado como proyecto de aprendizaje para practicar:

Automatización con Python.
Administración de sistemas Linux.
Comparación de configuraciones mediante snapshots.
Detección de archivos añadidos, eliminados y modificados.
Generación automática de reportes.
Organización y documentación de proyectos técnicos en GitHub.

El proyecto no pretende sustituir soluciones como AIDE, auditd o Wazuh, sino demostrar una implementación propia de un flujo básico de auditoría basado en snapshots y generación automática de reportes.
