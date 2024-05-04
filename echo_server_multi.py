import socket
import threading
import echo_protocol as echo
 
print("Welcome to Echo Server!")

IP = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((IP, echo.PORT))
sock.listen()

clienti = []

def new_game(client1, client2):
    clienti.remove(client1)
    clienti.remove(client2)
    print(f"Thread for handling game:")
    c1wins = 0
    c2wins = 0
    players = [client1, client2]
    for p in players:
        p.send_msg(str(c1wins))
        p.send_msg(str(c2wins))

    accepted_picks = ["piatra", "hartie", "foarfeca"]
    while c1wins < 3 and c2wins < 3:
        for p in players:   
            p.send_msg(str(c1wins))
            p.send_msg(str(c2wins))
            p.send_msg("Pick and wait for your opponent: ")
        c1rcvd = client1.recv_msg()
        c2rcvd = client2.recv_msg()
        if c1rcvd in accepted_picks and c2rcvd in accepted_picks:
            if c1rcvd == c2rcvd:
                for p in players:
                    p.send_msg("Draw")
            if c1rcvd == "piatra" and c2rcvd == "hartie":
                client1.send_msg("Ai pierdut")
                client2.send_msg("Ai castigat")
                c2wins = c2wins + 1
            elif c1rcvd == "piatra" and c2rcvd == "foarfeca":
                client1.send_msg("Ai castigat")
                client2.send_msg("Ai pierdut")
                c1wins = c1wins + 1
            if c1rcvd == "hartie" and c2rcvd == "foarfeca":
                client1.send_msg("Ai pierdut")
                client2.send_msg("Ai castigat")
                c2wins = c2wins + 1
            elif c1rcvd == "hartie" and c2rcvd == "piatra":
                client1.send_msg("Ai castigat")
                client2.send_msg("Ai pierdut")
                c1wins = c1wins + 1
            if c1rcvd == "foarfeca" and c2rcvd == "piatra":
                client1.send_msg("Ai pierdut")
                client2.send_msg("Ai castigat")
                c2wins = c2wins + 1
            elif c1rcvd == "foarfeca" and c2rcvd == "hartie":
                client1.send_msg("Ai castigat")
                client2.send_msg("Ai pierdut")
                c1wins = c1wins + 1
        else:
            for p in players:
                p.send_msg("Pick not accepted")
    for p in players:   
            p.send_msg(str(c1wins))
            p.send_msg(str(c2wins))
 
while True:
    print("Ready to accept a client connection.")
    client_sock, addr = sock.accept()
    print(f"Accepted new client connection: {addr}")
    client = echo.SocketWrapper(client_sock)
    clienti.append(client)
    if len(clienti) < 2:
        client.send_msg("Wait for an opponent...")
    else:
        client.send_msg("Starting game...")
        th = threading.Thread(target=new_game, args=(clienti[0], clienti[1]), daemon=True)
        th.start()