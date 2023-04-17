# Python Socket 詳細介紹

### Socket 
* Socket 是一個網路通訊的端點，它是一個虛擬的檔案，通過它可以實現不同主機間的通訊。
* Socket 有兩種，一種是服務端的 Socket，另一種是客戶端的 Socket。
* 服務端 Socket 會等待客戶端的 Socket 連接，而客戶端 Socket 會主動連接服務端 Socket。


socket格式：socket(family, type[,protocal])

socket 參數 | 說明
:--- | :---
socket.AF_UNIX | 用於同一台機器上的進程通信(UNIX域socket)
socket.AF_INET | 用於Internet進程間通信(IPv4)
socket.AF_INET6 | 用於Internet進程間通信(IPv6)
socket.SOCK_STREAM | 基於TCP的協議socket通信
socket.SOCK_DGRAM | 基於UDP的協議socket通信
socket.SOCK_RAW | 原始socket，普通的socket無法處理ICMP、IGMP等網絡協定，而SOCK_RAW可以；此外，SOCK_RAW也可以處理特殊的IPv4協定；此外還原始套接字可以設置IP_HDRINCL套接字選項，可以由用戶創建IP首部。
socket.SOCK_SEQPACKET | 可靠的連接序列封包資料傳輸

TCP Socket：
``` Python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
* TCP Socket 是一種面向連接的 Socket，通過三次握手建立一條可靠的數據傳輸通道，並且通過四次握手斷開連接。

UDP Socket：
``` Python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```
* UDP Socket 是一種無連接的 Socket，它只是把數據從一個地方發送到另一個地方，並不保證可靠性，因此使用 UDP 協議時，應用程序要自己處理丟包的情況。

**伺服器端 Socket 方法**

Server 方法 | 說明
:--- | :---
s.bind(address) | 將套接字綁定到地址。address地址的格式取決於地址族。在AF_INET下，以元組（host,port）的形式表示地址。
s.listen(backlog) | 開始TCP監聽。backlog指定在拒絕連接之前，可以掛起的最大連接數。該值至少為1，大部分應用設置為5就可以了。
s.accept() | 被動接受TCP客戶端連接，等待連接的請求（拜訪）。一旦連接到達，就建立新的套接字對象代表該連接並返回該套接字和客戶端的地址。返回的套接字對象可以用來收發數據。addr是客戶端的地址。

**客户端 Socket 方法**

Client 方法 | 說明
:--- | :---
s.connect(address) | 與遠程主機地址連接，address地址的格式取決於地址族。在AF_INET下，以元組（host,port）的形式表示地址。
s.connect_ex(address) | connect()函數的擴展版本，出錯時返回出錯代碼，而不是抛出異常。

**公共 Socket 方法**

Socket 方法 | 說明
:--- | :---
s.recv(bufsize[, flag]) | 接受TCP套接字的數據。數據以字符串形式返回，bufsize指定要接受的最大數據量。flag提供有關消息的其他信息，通常可以忽略。
s.send(string[, flag]) | 完整發送TCP數據，將字符串中的數據發送到鏈接的套接字，但在返回之前嘗試發送所有數據。成功返回None，失敗則拋出異常
s.sendall(string[, flag]) | 發送TCP數據，將字符串中的數據發送到鏈接的套接字，但在返回之前嘗試發送所有數據。成功返回None，失敗則拋出異常
s.recvfrom(bufsize[, flag]) | 接受UDP數據，和recv()類似，但返回值是（data, address）。其中data是包含接收數據的字符串，address是發送數據的套接字地址。
s.sendto(string[, flag], address) | 發送UDP數據，將數據發送到套接字，address是形式為（ipaddr，port）的元組，指定遠程地址。返回值是發送的字節數。注意，如果使用IPv4，ipaddr應該是字符串，如'13'
s.close() | 關閉套接字
s.getpeername() | 返回套接字對方的地址，返回值通常是一個tuple(ipaddr, port)
s.getsockname() | 返回套接字自己的地址，通常是一個tuple(ipaddr, port)
s.setsockopt(level, optname, value) | 設置給定套接字選項的值
s.getsockopt(level, optname[, buflen]) | 返回套接字選項的值
s.settimeout(timeout) | 設置套接字操作的超時期，timeout是一個浮點數，單位是秒。值為None表示沒有超時期。一般，超時期應該在創建套接字時設置，因為它們可能用於連接的操作（如client的connect()）
s.gettimeout() | 返回當前超時期的值，單位是秒，如果沒有設置超時期，則返回None
s.fileno() | 返回套接字的文件描述
s.setblocking(flag) | 如果flag為0，則將套接字設置為非阻塞模式，否則將套接字設置為阻塞模式（默認值）
s.makefile() | 創建一個和套接字相關的文件

### 簡單建立SERVER端

**TCP 伺服器**

1、創建伺服器端
``` Python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind()
```

2、開始監聽
``` Python
s.listen()
```

3、無限迴圈接受客戶端連線
``` Python
While True:
    s.accept()
```

4、接收客戶端傳來的資料，發送資料給客戶端
``` Python
s.recv()
s.sendall()
```

5、傳輸完畢後，關閉Socket
``` Python
s.close()
```

**TCP 客户端**

1、創建客户端
``` Python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect()
```

2、接收伺服器端傳來的資料，發送資料給伺服器端
``` Python
s.sendall()
s.recv()
```

3、傳輸完畢後，關閉Socket
``` Python
s.close()
```

### Socket 伺服器端程式碼

``` Python
import socket

HOST = '192.168.1.100'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    conn, addr = s.accept()
    print 'Connected by ', addr

    while True:
        data = conn.recv(1024)
        print data

        conn.send("server received you message.")

# conn.close()
```

### Socket 客戶端程式碼

``` Python
import socket
HOST = '192.168.1.100'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = raw_input("Please input msg:")
    s.send(cmd)
    data = s.recv(1024)
    print data

    #s.close()
```