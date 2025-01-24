from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/metrics')
def metrics():
    try:
        # Fetch system metrics
        cpu_percent = psutil.cpu_percent(interval=0.5)
        memory_percent = psutil.virtual_memory().percent
        disk_percent = psutil.disk_usage('/').percent

        # Return metrics as JSON
        return jsonify({
            'cpu_percent': cpu_percent,
            'memory_percent': memory_percent,
            'disk_percent': disk_percent
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
