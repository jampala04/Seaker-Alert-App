import psutil
import time
import smtplib
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['DEBUG'] = False  

def get_system_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(),
        "ram_usage": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "disk_usage": round(psutil.disk_usage('/').used / (1024 ** 3), 2),
        "uptime": round((time.time() - psutil.boot_time()) / 3600, 2)
    }
    return metrics

def send_email_alert(subject, body):
    sender = "your_email@gmail.com"
    recipient = "recipient_email@gmail.com"
    password = "your_email_password"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, message)
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_thresholds(metrics):
    if metrics["cpu_usage"] > 80:
        send_email_alert("High CPU Usage Alert", f"CPU usage is {metrics['cpu_usage']}%")
    if metrics["ram_usage"] > 4:  #  if RAM usage > 4 GB
        send_email_alert("High RAM Usage Alert", f"RAM usage is {metrics['ram_usage']} GB")

@app.route('/api/metrics')
def api_metrics():
    metrics = get_system_metrics()
    check_thresholds(metrics)
    return jsonify(metrics)
@app.route('/')

def dashboard():
    return render_template('ALERT.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)