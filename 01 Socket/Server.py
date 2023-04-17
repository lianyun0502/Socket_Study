from __future__ import annotations
import socket
import sys
import time
import typing

HOST = '0.0.0.0'
PORT = 7000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)


print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')


def handler_accept(conn:socket)->typing.Any:
    in_data = conn.recv(1024)
    print(f'recv: {in_data.decode()}')

    out_data = f'echo {in_data.decode()}'
    conn.send(out_data.encode())
    return in_data.decode()

# server.setblocking(False) # 預設為 blocking, 這裡設為 non-blocking
# while True:
#     try:
#         conn, addr = server.accept() # 當設為 non-blocking 時, 否則沒有accept時會阻塞在這行
#         print(f'connected by {str(addr)}')
#         i=0
#         while i < 10000:
#             i += 1
#             out_data = f'echo {i}'
#             conn.send(out_data.encode())
#             time.sleep(0.5)
#         break
#     except BlockingIOError as e:
#         print(f'no connection {e}')
#         time.sleep(1)
#         continue

while True:
    conn, addr = server.accept()
    print(f'connected by {str(addr)}')
    while True:
        in_data = handler_accept(conn)
        if in_data.upper() == 'Q':
            break
    if in_data.upper() == 'Q':
        break

sys.exit(server.close())