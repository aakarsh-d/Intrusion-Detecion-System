// Example: Adding some dynamic content into the process and network sections
document.addEventListener("DOMContentLoaded", function() {
    // Mock data for processes
    const processes = [
        { name: 'python3', pid: 12345 },
        { name: 'bash', pid: 23456 },
        { name: 'firefox', pid: 34567 },
        { name: 'node', pid: 45678 },
    ];

    const networkConnections = [
        { local_ip: '127.0.0.1', remote_ip: '192.168.1.2', pid: 12345 },
        { local_ip: '127.0.0.1', remote_ip: '192.168.1.3', pid: 23456 },
    ];

    const processList = document.getElementById('process-list');
    const networkList = document.getElementById('network-list');

    processes.forEach(proc => {
        const li = document.createElement('li');
        li.textContent = `${proc.name} (PID: ${proc.pid})`;
        processList.appendChild(li);
    });

    networkConnections.forEach(conn => {
        const li = document.createElement('li');
        li.textContent = `Local: ${conn.local_ip}:${conn.pid} → Remote: ${conn.remote_ip}`;
        networkList.appendChild(li);
    });

    // Using GSAP for smooth animation on load
    gsap.from('.status-box', { duration: 1, opacity: 0, y: -50, stagger: 0.2 });
});
