import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        URL = urlparse(self.path)
        
        if URL.path == "/hand":
            p = parse_qs(URL.query)
            login = p.get("login", [""])[0]
            password = p.get("password", [""])[0]
            
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            html = f"""<!DOCTYPE html><html><body>
            <h3>Получено:</h3>
            <p>Login: {login}</p>
            <p>Password: {password}</p>
            <a href="/index.html">Вернуться на главную</a>
            </body></html>"""
            self.wfile.write(html.encode("utf-8"))
            return
        
        super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"server start: http://localhost:{PORT}")
        httpd.serve_forever()