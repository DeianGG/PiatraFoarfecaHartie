import socket
import echo_protocol as echo
import sys
 
IP = '127.0.0.1'
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

sock_wrapper = echo.SocketWrapper(sock)

rcvd = sock_wrapper.recv_msg()
print(rcvd)

c1wins = int(sock_wrapper.recv_msg())
c2wins = int(sock_wrapper.recv_msg())

while True:
    if rcvd == "Wait for an opponent...":
        c1wins = int(sock_wrapper.recv_msg())
        c2wins = int(sock_wrapper.recv_msg())
    else:
        c2wins = int(sock_wrapper.recv_msg())
        c1wins = int(sock_wrapper.recv_msg())

    print('Scor:'+str(c1wins)+' '+str(c2wins))
    if c2wins == 3 or c1wins == 3:
        break
    msg = sock_wrapper.recv_msg()

    pick = input(msg)
    sock_wrapper.send_msg(pick)
    rez = sock_wrapper.recv_msg()
    print(rez)
if c1wins == 3:
    print("Ai castigat meciul!")
else:
    print("Ai pierdut meciul")
    
 
 
sock.close()
sys.exit()