from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class DevOpsHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "Python DevOps Pipeline"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>My First DevOps Project</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin-top: 100px;
                        background: #f4f7fb;
                    }
                    .card {
                        background: white;
                        padding: 35px;
                        margin: auto;
                        max-width: 550px;
                        border-radius: 12px;
                        box-shadow: 0 4px 15px #0001;
                    }
                    h1 { color: #2563eb; }
                    p { color: #444; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h1>My First DevOps Project</h1>
                    <p>Python application is running!</p>
                    <p>Built with Docker and GitHub Actions.</p>
                    <p>Status: <strong>Running</strong></p>
                </div>
            </body>
            </html>
            """

            self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), DevOpsHandler)
    print("Application running on port 8000")
    server.serve_forever()