import socket 
import sys 

try: 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Successfully Created")
except socket.error as err:
    print(f"Socket creation failed as {err}")

#create a default port 
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror as err: 
    print("There was an error ")
    sys.exit()

s.connect((host_ip,port))

print(f"Succesffuly connected to www.google.com on port {host_ip}")

