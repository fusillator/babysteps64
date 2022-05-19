import socket
import os
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("scrap",55554))
    
    pid=os.fork()
    if pid > 0:
        while True:
            data=s.recv(4096)
            print(data.decode("utf-8"),end="")
    else:
        while True:
            cmd=input()+"\n"
            s.send(cmd.encode("utf-8"))

