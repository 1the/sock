from socket import *
try:
    s = socket(AF_INET , SOCK_STREAM)
    host = '127.0.0.1'
    port = 4000
    s.bind((host , port))
    s.listen(5)
    session , addr = s.accept()
    print("got connection from", addr[0])
    while True:
        # receive
        data = b''      # to store data larger than chunk size :2048
        while True:     # receiving a message larger than 2048
            x = session.recv(2048)
            data += x.decode()      # concatenate after decoding
            if len(x) < 2048 :
                break       # we dont have to loop if the size is already smaller
        print("client sent: ",data)
        # send
        y = input("enter a message")
        chunk = 2048  # divide message into smaller chunks
        total = len(y)  # total length of message
        sent = 0  # actual sent size
        while sent < total:  # repeat as long as the sent size is nt equal to message size
            msg = y[sent:sent + chunk]
            session.send(msg.encode())
            sent += len(msg)

    session.close()

except error as e:
    print(e)