from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from app import BaseMLModel
import use

models = {}

# basic server

HOSTNAME = "localhost"
PORT = 8080

class BasicServer(BaseHTTPRequestHandler):

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        request_body = json.loads(self.rfile.read(content_len))
        print(models)
        self.send_response(200)
        self.end_headers()
        try:
            result = models[request_body['model_name']](**request_body['data'])
            self.wfile.write(result.encode("utf-8"))
        except:
            self.wfile.write('A problem has occured!!'.encode("utf-8"))
        


if __name__ == "__main__":        
    webServer = HTTPServer((HOSTNAME, PORT), BasicServer)
    print("Server started http://%s:%s" % (HOSTNAME, PORT))
    
    # init models with classes functions
    for cls in BaseMLModel.__subclasses__():
        models[cls.__name__] = cls().get_results

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")