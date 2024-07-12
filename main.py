from flask import Flask, url_for
from prometheus_flask_exporter import PrometheusMetrics
import time
import socket

app = Flask(__name__,
            static_url_path='',
            static_folder='static')
metrics = PrometheusMetrics(app)


@app.route("/")
def service():
    return (
        "<title>Simple HTTP Server</title>"
        f"<link rel=\"shortcut icon\" href=\"{url_for('static', filename='favicon.ico')}\">"
        "<body>"
        f"<p><b>timestamp: </b> {time.time()}</p>"
        f"<p><b>hostname: </b> {socket.gethostname()}</p>"
        "</body>"
    )


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
