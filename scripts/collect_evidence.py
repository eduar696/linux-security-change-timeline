import os
import shutil
import pwd
from datetime import datetime

# Configuracion de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_DIR = os.path.join(BASE_DIR, 'evidence')

FILES_TO_COLLECT = [
    '/etc/passwd',
    '/etc/ssh/sshd_config',
    '/etc/ufw/user.rules'
]

def fix_ownership(path):
    """Cambia el dueño de la carpeta recolectada al usuario que ejecutó sudo."""
    sudo_user = os.environ.get('SUDO_USER')
    if sudo_user:
        user_info = pwd.getpwnam(sudo_user)
        uid = user_info.pw_uid
        gid = user_info.pw_gid
        # Cambia el dueño de la carpeta y todo su contenido
        for root, dirs, files in os.walk(path):
            os.chown(root, uid, gid)
            for f in files:
                os.chown(os.path.join(root, f), uid, gid)
        print(f"[*] Propiedad restaurada al usuario: {sudo_user}")

def collect():
    # Crear carpeta con fecha
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot_dir = os.path.join(EVIDENCE_DIR, timestamp)
    
    os.makedirs(snapshot_dir, exist_ok=True)
    print(f"[*] Iniciando recolección en: {snapshot_dir}")

    for file_path in FILES_TO_COLLECT:
        if os.path.exists(file_path):
            try:
                dest = os.path.join(snapshot_dir, os.path.basename(file_path))
                shutil.copy2(file_path, dest)
                print(f"[+] Recolectado: {file_path}")
            except Exception as e:
                print(f"[!] Error al copiar {file_path}: {e}")
        else:
            print(f"[!] Archivo no encontrado: {file_path}")

    # Si se ejecutó con sudo, reparamos los permisos
    if os.geteuid() == 0:
        fix_ownership(snapshot_dir)

    print("[*] Recolección finalizada.")

if __name__ == "__main__":
    collect()
