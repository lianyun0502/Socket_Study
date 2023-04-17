import socket
HOST = '192.168.1.106'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))



while True:
    out_data = input('press enter to send: ')
    print(f'send: {out_data}')
    s.send(out_data.encode())
    in_data = s.recv(1024)
    print(f'recv: {in_data.decode()}')
    if out_data.upper() == 'Q':
        break

s.close()