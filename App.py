from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name
    name = "Priya"
    
    # System Username
    username = os.getenv('USER') or os.getenv('USERNAME')
    
    # Server Time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    server_time = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

    # Get 'top' command output
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -15", shell=True).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    # HTML response
    return f"""
    <html>
        <head><title>/htop</title></head>
        <body>
            <h2>System Info</h2>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time:</strong> {server_time}</p>
            <h3>Top Output:</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)