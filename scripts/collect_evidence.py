import os
import shutil
from datetime import datetime

# Configuracion de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_DIR = os.path.join(BASE_DIR, 'evidence')

# Archivos que queremos rastrear
FILES_TO_COLLECT = [
    '/etc/passwd',
    '/etc/ssh/sshd_config',
    '/etc/ufw/user.rules' # Ajusta si tu ruta de UFW es distinta
]

def collect():
    # Crear una carpeta con la fecha actual
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

    print("[*] Recolección finalizada.")

if __name__ == "__main__":
    collect()
