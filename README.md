# Linux Security Change Timeline

Este proyecto es una herramienta de auditoría forense diseñada para reconstruir la historia de seguridad de un sistema Linux. En lugar de realizar escaneos en tiempo real, el sistema genera una línea de tiempo (timeline) basada en la captura y análisis de snapshots de configuración, permitiendo identificar cuándo, cómo y qué cambios alteraron la postura de seguridad del servidor.

## Contexto y Motivación
Muchas brechas de seguridad no ocurren por exploits de día cero o ataques sofisticados, sino por la "deriva de configuración" (Configuration Drift): cambios silenciosos realizados por administradores o procesos automatizados que pasan desapercibidos hasta que es demasiado tarde.

Este proyecto ataca el problema desde la **trazabilidad**:
- ¿Cuándo se habilitó el acceso SSH para root?
- ¿Qué usuario con privilegios fue añadido y cuándo?
- ¿En qué momento se desactivó el firewall?

## Arquitectura del Proyecto

El proyecto sigue una metodología de **captura y análisis**:

1. **Capa de Evidencia (`evidence/`):** Almacena snapshots incrementales de archivos de configuración y estados del sistema.
2. **Capa de Recolección (`scripts/collect_evidence.py`):** Agente que extrae el estado actual del sistema y lo persiste.
3. **Capa de Análisis (`scripts/build_timeline.py`):** Motor que procesa la evidencia, detecta diferencias (diffs) y genera una línea de tiempo cronológica.
4. **Capa de Reporte (`timeline/`):** Genera un informe Markdown auditable.

## Evidencia Visual
A continuación se muestra una captura de pantalla que demuestra la funcionalidad central de la herramienta: la detección automática de una desviación de configuración en el archivo `sshd_config`.

![Evidencia de detección de cambio](screenshots/auditoria_deteccion_cambio.png)

## Vectores de Análisis
El sistema rastrea los siguientes elementos críticos:
- **Identidad:** Usuarios creados y grupos modificados (`/etc/passwd`, `/etc/group`).
- **Acceso:** Cambios en la configuración de SSH (`/etc/ssh/sshd_config`).
- **Red:** Estado del Firewall (ufw, iptables).
- **Servicios:** Servicios del sistema habilitados o desactivados (`systemctl`).

## Uso

### 1. Recolección de evidencia
Ejecuta el script con `sudo` para permitir el acceso a los archivos de configuración protegidos:

```
sudo python3 scripts/collect_evidence.py
```
_Nota: El script restaurará automáticamente los permisos de los archivos generados a tu usuario actual._


### 2. Generación del Timeline

Una vez que tengas varias capturas en el tiempo, ejecuta el motor de análisis para comparar los estados y generar el reporte:

```
python3 scripts/build_timeline.py

```
El resultado se generará en timeline/timeline.md


### Requisitos
- **Python 3.x**
- **Privilegios:** El script requiere privilegios elevados (`sudo`) para acceder a archivos protegidos del sistema (ej. `/etc/ufw/user.rules`). El script gestiona automáticamente la restauración de permisos tras la recolección.

    
## Consideraciones de Seguridad
Esta herramienta está diseñada para entornos de auditoría. Para garantizar una recolección completa, el script requiere ejecución con `sudo`. Hemos implementado una **función de seguridad de restauración de propiedad**: tras la recolección, el script devuelve automáticamente la propiedad de los archivos al usuario original, asegurando que se mantenga el principio de menor privilegio y permitiendo la gestión posterior de los archivos sin necesidad de privilegios administrativos.

---
*Desarrollado como proyecto de auditoría de sistemas Linux.*
