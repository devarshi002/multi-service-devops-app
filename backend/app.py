from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class APIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api":
            data = {
                "message": "Hello from Devarshi's Backend API!",
                "status": "success"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

server = HTTPServer(("0.0.0.0", 5000), APIHandler)
print("Backend API running on port 5000", flush=True)
server.serve_forever()
