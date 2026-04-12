import http.server
import urllib.request
import urllib.error
import json
import os

PORT = 8731

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def do_POST(self):
        if self.path in ('/proxy/claude', '/proxy/chatgpt', '/proxy/dalle'):
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            api_key = self.headers.get('x-api-key', '')
            if self.path == '/proxy/claude':
                url = 'https://api.anthropic.com/v1/messages'
                headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': api_key,
                    'anthropic-version': '2023-06-01',
                }
            elif self.path == '/proxy/dalle':
                url = 'https://api.openai.com/v1/images/generations'
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {api_key}',
                }
            else:
                url = 'https://api.openai.com/v1/chat/completions'
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {api_key}',
                }
            try:
                req = urllib.request.Request(url, data=body, headers=headers, method='POST')
                with urllib.request.urlopen(req) as resp:
                    result = resp.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self._cors()
                self.end_headers()
                self.wfile.write(result)
            except urllib.error.HTTPError as e:
                err_body = e.read()
                self.send_response(e.code)
                self.send_header('Content-Type', 'application/json')
                self._cors()
                self.end_headers()
                self.wfile.write(err_body)
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self._cors()
                self.end_headers()
                self.wfile.write(json.dumps({'error': {'message': str(e)}}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, x-api-key, x-model, Authorization')

    def log_message(self, fmt, *args):
        pass


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f'Multi-AI Tool running at http://localhost:{PORT}/multi-ai.html')
    print('Keep this window open while using the tool. Close it when done.')
    with http.server.HTTPServer(('', PORT), Handler) as httpd:
        httpd.serve_forever()
