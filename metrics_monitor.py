import psutil
import time
import os
from datetime import datetime

def get_cpu_usage():
    """Get CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    """Get RAM usage in GB."""
    ram = psutil.virtual_memory()
    return ram.used / (1024 ** 3)

def get_disk_usage():
    """Get Disk usage in GB."""
    disk = psutil.disk_usage('/')
    return disk.used / (1024 ** 3)

def get_uptime():
    """Get system uptime in hours."""
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    return uptime.total_seconds() / 3600

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def collect_metrics():
    """Collect and print system metrics."""
    clear_screen()  # Clear the screen before printing metrics
    print(f"{'Metric':<20} {'Value':<10}")
    print("-" * 30)
    print(f"{'CPU Usage (%)':<20} {get_cpu_usage():<10.2f}")
    print(f"{'RAM Usage (GB)':<20} {get_ram_usage():<10.2f}")
    print(f"{'Disk Usage (GB)':<20} {get_disk_usage():<10.2f}")
    print(f"{'Uptime (hours)':<20} {get_uptime():<10.2f}")

if __name__ == "__main__":
    while True:
        collect_metrics()  # Collect and display metrics
        time.sleep(5)  # Wait for 5 seconds before updating
