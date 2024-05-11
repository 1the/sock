from socket import *
try:
    s = socket(AF_INET , SOCK_STREAM)
    host = '127.0.0.1'
    port = 4000
    s.connect((host , port))
    while True:
        # send
        # s.send(input("enter a message").encode())  # normal way to send
        y = input("enter a message")
        chunk = 2048        # divide message into smaller chunks
        total = len(y)      # total length of message
        sent = 0            # actual sent size
        while sent < total:     # repeat as long as the sent size is nt equal to message size
            msg = y[sent:sent + chunk]
            s.send(msg.encode())
            sent += len(msg)
        # receive
        data = b''  # to store data larger than chunk size :2048
        while True:  # receiving a message larger than 2048
            x = s.recv(2048)
            data += x.decode()  # concatenate after decoding
            if len(x) < 2048:
                break  # we dont have to loop if the size is already smaller
        print("server sent: ", data)
         # x = s.recv(2048) # normal way to receive up to 2048 bytes
        # print("server sent: ",x.decode())
    s.close()

except error as e:
    print(e)




