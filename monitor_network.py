import psutil

def check_network_connections(allowed_ips):
    suspicious = []
    connections = psutil.net_connections(kind='inet')
    for conn in connections:
        if conn.raddr:  # Check if connection has remote address
            ip = conn.raddr.ip
            if ip not in allowed_ips:
                suspicious.append({
                    'pid': conn.pid,
                    'local_ip': conn.laddr.ip,
                    'local_port': conn.laddr.port,
                    'remote_ip': ip,
                    'remote_port': conn.raddr.port
                })
    return suspicious
