from flask import Flask
from http.server import BaseHTTPRequestHandler

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Kal"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        response = app.test_client().get('/')
        self.wfile.write(response.data)
        return
