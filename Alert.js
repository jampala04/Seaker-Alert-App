function updateMetrics() {
    fetch('/api/metrics')
        .then(response => response.json())
        .then(data => {
            document.getElementById('cpu_usage').textContent = data.cpu_usage;
            document.getElementById('ram_usage').textContent = data.ram_usage;
            document.getElementById('disk_usage').textContent = data.disk_usage;
            document.getElementById('uptime').textContent = data.uptime;
            if (data.cpu_usage > 80 || data.ram_usage > 4) {
                document.getElementById('alert').style.display = 'block';
                document.getElementById('alert_message').textContent = `High resource usage detected! CPU: ${data.cpu_usage}% | RAM: ${data.ram_usage} GB`;
            } else {
                document.getElementById('alert').style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error fetching metrics:', error);
        });
}