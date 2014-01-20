from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import platform
import os



# OS version
out1 = platform.platform()

# kernel version, compile date
out2 = os.listdir("/lib/modules")

# interpret. python version
out3 = platform.python_version()

# RAM state
out4 = os.popen("cat /proc/meminfo").read().replace('kB', 'kB <br>') 

# top 10 processes
# uptime
# free disks


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write('<title>Indigo Timofey Task #1 script</title>')
        self.wfile.write(out1)
        self.wfile.write('<br>')
        self.wfile.write(out2)
        self.wfile.write('<br>')
        self.wfile.write(out3)
        self.wfile.write('<br>')
        self.wfile.write(out4)

serv = HTTPServer(("localhost",86),HttpProcessor)
serv.serve_forever()
