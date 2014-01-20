import HTTPServer, CGIHTTPRequestHandler
 
adr=('',80)
server=HTTPServer(adr,CGIHTTPRequestHandler)
server.serve_forever()

