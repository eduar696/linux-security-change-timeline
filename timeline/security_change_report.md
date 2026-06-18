```markdown
# Reporte de Auditoría: Ejemplo de Cambio

**Fecha:** 2026-06-17

## Comparación: 2026-06-17_13-26-37 -> 2026-06-17_14-16-23

### Cambio detectado en: `sshd_config`
Se detectó una modificación en la configuración del servicio SSH.

```diff
--- Anterior
+++ Actual
@@ -120,3 +120,4 @@
 #      AllowTcpForwarding no
 #      PermitTTY no
 #      ForceCommand cvs server
+# --- CAMBIO DETECTADO: PermitRootLogin no ---

