from socket import *
import json

serverName = "localhost"
serverPort = 16500
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


try:
    while True:
        function= input("Random,Add,Subtract")
        
        if function == "exit":
            break
        
        try:
            num1 = int(input("num1:"))
            num2 = int(input("num2:"))
        except ValueError:
            print("Fejl")    
            continue
        
        textJson = {"function": function, "num1": num1 if function in ["Random","Add","Subtract"]else None}
        
        clientSocket.send(json.dumps(textJson).encode())
        recvJson = clientSocket.recv(1024).decode()
        recv = json.loads(recvJson)
        
except KeyboardInterrupt:
    pass
finally:
    clientSocket.close()