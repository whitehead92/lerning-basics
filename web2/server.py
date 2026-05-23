import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import json

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        URL = urlparse(self.path)
        
        if URL.path == "/hand":
            p = parse_qs(URL.query)
            login = p.get("login", [""])[0]
            password = p.get("password", [""])[0]
            
            self._result(login, password)
            return
            
        if self.path == "/":
            self.path = "/index.html"
        super().do_GET()
        
    def do_POST(self):
        URL = urlparse(self.path)
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        
        if URL.path == "/auth":
            data = parse_qs(body)
            login = data.get("login", [""])[0]
            password = data.get("password", [""])[0]
            self._result(login, password)
            
        elif URL.path == "/auth-json":
            data = json.loads(body)
            login = data.get("login", "")
            password = data.get("password", "")
            self._result(login, password)
        else:
            self.send_response(404)
            self.end_headers()

    def _result(self, login, password):
        html = f"""<!DOCTYPE html><html><body>
        <h3>Получено:</h3>
        <p>Login: {login}</p>
        <p>Password: {password}</p>
        <a href="/index.html">Вернуться на главную</a>
        </body></html>"""
        
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))
        
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"server start: http://localhost:{PORT}")
        httpd.serve_forever()