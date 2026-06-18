import os
import difflib

# Rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVIDENCE_DIR = os.path.join(BASE_DIR, 'evidence')
TIMELINE_FILE = os.path.join(BASE_DIR, 'timeline', 'timeline.md')

def get_snapshots():
    # Listar carpetas y ordenarlas por nombre (fecha)
    return sorted([d for d in os.listdir(EVIDENCE_DIR) 
                   if os.path.isdir(os.path.join(EVIDENCE_DIR, d))])

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        diff = difflib.unified_diff(
            f1.readlines(), f2.readlines(),
            fromfile='Anterior', tofile='Actual', lineterm=''
        )
    return list(diff)

def build():
    snapshots = get_snapshots()
    if len(snapshots) < 2:
        print("[!] Se necesitan al menos dos snapshots para generar una línea de tiempo.")
        return

    with open(TIMELINE_FILE, 'w') as report:
        report.write("# Security Audit Timeline\n\n")
        
        # Comparar pares: (snap1, snap2), (snap2, snap3)...
        for i in range(len(snapshots) - 1):
            snap_old = snapshots[i]
            snap_new = snapshots[i+1]
            report.write(f"## Comparación: {snap_old} -> {snap_new}\n\n")
            
            # Buscar archivos comunes en ambas carpetas
            dir1 = os.path.join(EVIDENCE_DIR, snap_old)
            dir2 = os.path.join(EVIDENCE_DIR, snap_new)
            files = set(os.listdir(dir1)) & set(os.listdir(dir2))
            
            for f in files:
                diffs = compare_files(os.path.join(dir1, f), os.path.join(dir2, f))
                if diffs:
                    report.write(f"### Cambio detectado en: `{f}`\n```diff\n")
                    report.write('\n'.join(diffs))
                    report.write("\n```\n")
    
    print(f"[*] Reporte generado exitosamente en: {TIMELINE_FILE}")

if __name__ == "__main__":
    build()
