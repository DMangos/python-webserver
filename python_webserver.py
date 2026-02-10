from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Set the directory to serve files from
os.chdir('/home/webserver')

# Define the server address and port
server_address = ('0.0.0.0', 8000)

# Create the server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Start the server
print("Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000) ...")
httpd.serve_forever()   
