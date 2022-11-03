import http.server
from prometheus_client import start_http_server, Counter

c = Counter('app_cloud_run', 'total http requests to cloud run app')

APP_PORT = 8000
METRICS_PORT = 8081

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        c.inc()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Cloud Run App</title></head><body><h1>Sample Cloud Run App</h1></body></html>", "utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()
