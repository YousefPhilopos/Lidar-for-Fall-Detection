from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import time

tasklist = ['Task 1', 'Task 2', 'Task 3']

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = '<html><body>'
            output += '<h1>List</h1>'
            output += '<h3><a href="/new">Add New Task</a></h3>'
            for task in tasklist:
                output += task
                output += '</br>'
            output += '</body></html>'
            self.wfile.write(output.encode())
        elif self.path == '/new':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = '<html><body>'
            output += '<h1>Add New Task</h1>'
            output += '<form method="POST" action="/new">'
            output += '<input name="task" type="text" placeholder="Add new task">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'
            self.wfile.write(output.encode())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == '/new':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            task = urllib.parse.parse_qs(post_data.decode("utf-8"))['task'][0]
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            tasklist.append(task + ", " + timestamp)
            if len(tasklist) > 10:
                del tasklist[0]
            self.send_response(301)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_error(404)

def main():
    PORT = 8000
    server_address = ('10.0.0.212', PORT) # use the IP address of the computer running the server
    server = HTTPServer(server_address, requestHandler)
    print('Server running on port', PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()