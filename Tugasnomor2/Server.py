import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Waiting...")

client_socket, Client_address = server_socket.accept()
print(f"Terhubung dengan {Client_address}")

while True:
    pesan_dari_klien = client_socket.recv(1024).decode()
    if not pesan_dari_klien:
        break
    jumlah_karakter = str(len(pesan_dari_klien))
    client_socket.send(jumlah_karakter.encode())

client_socket.close()
server_socket.close()