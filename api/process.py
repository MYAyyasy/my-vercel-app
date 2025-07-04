from http.server import BaseHTTPRequestHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):  # Tangani preflight request
        self.send_response(204)  # No Content
        self.send_header("Access-Control-Allow-Origin", "https://myayyasy.github.io")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "https://myayyasy.github.io")  # Spesifik ke domain Anda
        self.end_headers()
        
        # Proses data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        response = {"status": "success", "data": json.loads(post_data)}
        self.wfile.write(json.dumps(response).encode())
