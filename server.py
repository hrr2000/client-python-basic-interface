from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from app import BaseMLModel
import use

# will store subclasses of BaseMLModel
models = {}

# basic server
HOSTNAME = "localhost"
PORT = 8080
ERROR_MESSAGE = "A problem has occured!!"

class BasicServer(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        request_body = json.loads(self.rfile.read(content_len))
        self.send_response(200)
        self.end_headers()
        try:
            result = models[request_body['model_name']](**request_body['data'])
            self.wfile.write(result.encode("utf-8"))
        except:
            self.wfile.write(ERROR_MESSAGE.encode("utf-8"))
        

if __name__ == "__main__":        
    web_server = HTTPServer((HOSTNAME, PORT), BasicServer)
    print("Server started http://%s:%s" % (HOSTNAME, PORT))
    
    # init models with classes functions
    for cls in BaseMLModel.__subclasses__():
        models[cls.__name__] = cls().get_results

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")
    
