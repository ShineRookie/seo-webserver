from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

import pymorphy2 


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    __image = None

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        if self.path == '/index.html':
            try:
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.end_headers()
                image_tag = 'Image not found' if SimpleHTTPRequestHandler.__image is None or SimpleHTTPRequestHandler.__image == '' else SimpleHTTPRequestHandler.__image
                self.wfile.write(bytes(file_to_open.format(image=image_tag), 'utf-8'))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b'404 - Not Found')
        else:
            self.send_response(200)
            self.end_headers()
            with open(self.path[1:], 'rb') as file:
                content = file.read()
            self.wfile.write(content)

    def do_POST(self):
        search_params = self.path.split('?')[1].split('&')

        if self.path.startswith('/search'):

            search_text = urllib.parse.unquote(search_params[0])
            SimpleHTTPRequestHandler.__image = parse_images('images.html', search_text).strip()
            self.send_response(200)
            self.end_headers()


class Server:
    @staticmethod
    def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
        server_address = ('127.0.0.1', 666)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()


if __name__ == "__main__":
    Server.run()
