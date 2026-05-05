# Starter Code for Standard Library Web API Assignment

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse

items = [
    {"id": 1, "name": "Notebook", "description": "A simple paper notebook."},
    {"id": 2, "name": "Pen", "description": "A blue ink ballpoint pen."}
]

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def _write_json(self, data):
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/items":
            self._set_headers(200)
            self._write_json({"items": items})
            return

        if parsed_path.path.startswith("/items/"):
            item_id = parsed_path.path.split("/")[-1]
            try:
                item_id = int(item_id)
            except ValueError:
                self._set_headers(400)
                self._write_json({"error": "Invalid item ID"})
                return

            item = next((item for item in items if item["id"] == item_id), None)
            if item:
                self._set_headers(200)
                self._write_json(item)
            else:
                self._set_headers(404)
                self._write_json({"error": "Item not found"})
            return

        self._set_headers(404)
        self._write_json({"error": "Not found"})

    def do_POST(self):
        if self.path == "/items":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                self._set_headers(400)
                self._write_json({"error": "Invalid JSON"})
                return

            if "id" not in data or "name" not in data:
                self._set_headers(400)
                self._write_json({"error": "Missing required fields"})
                return

            items.append(data)
            self._set_headers(201)
            self._write_json(data)
            return

        self._set_headers(404)
        self._write_json({"error": "Not found"})


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
