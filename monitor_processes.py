import psutil

def check_processes(whitelist):
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] not in whitelist:
                suspicious.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return suspicious
