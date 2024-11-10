import http.server
import socketserver

PORT = 8080

# Create handler for the server
Handler = http.server.SimpleHTTPRequestHandler

# Bind server to all interfaces (0.0.0.0) and port 8080
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Server running on http://0.0.0.0:{PORT}/")
    httpd.serve_forever()
