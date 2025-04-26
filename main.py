import time
from flask import Flask, render_template
from flask_socketio import SocketIO
import psutil
from monitor_processes import check_processes
from monitor_network import check_network_connections

# Flask setup
app = Flask(__name__)
socketio = SocketIO(app)

# Whitelist of allowed process names
process_whitelist = ['bash', 'python3', 'firefox']

# Whitelist of allowed remote IPs
allowed_ips = ['127.0.0.1', '192.168.1.1']  # Add your trusted IPs

@app.route('/')
def index():
    return render_template('index.html')

def monitor_system():
    while True:
        # Check for suspicious processes
        suspicious_processes = check_processes(process_whitelist)
        if suspicious_processes:
            socketio.emit('update_processes', {'data': suspicious_processes})
        
        # Check for suspicious network connections
        suspicious_connections = check_network_connections(allowed_ips)
        if suspicious_connections:
            socketio.emit('update_network_connections', {'data': suspicious_connections})

        time.sleep(10)  # Scan every 10 seconds

# Background thread to monitor system and send data via SocketIO
@socketio.on('connect')
def handle_connect():
    print("Client connected.")
    socketio.start_background_task(monitor_system)

if __name__ == '__main__':
    socketio.run(app, debug=True)
