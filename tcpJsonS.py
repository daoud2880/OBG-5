from socket import *
import threading 
import random
import json

def handleClient(connectionSocket, addr):
    
    print(str(addr) + "has connected") 
    sentence = connectionSocket.recv(1024).decode()
    try:
            
        jsonText = json.loads(sentence)
        
        function = jsonText.get("function")

        if function == "Random":
            num1 = jsonText.get("num1")
            num2 = jsonText.get("num2")
            randomNumber = random.randint(num1,num2)
            answer = {"result":randomNumber}
        elif function == "Add":
            num1 = jsonText.get("num1")
            num2 = jsonText.get("num2")
            sum = num1 + num2
            answer = {"result": sum}
        elif function == "Subtract":
            num1 = jsonText.get("num1")
            num2 = jsonText.get("num2")
            sum = num1 - num2
            answer = {"result":sum}
        else:
            answer = {"Mistake":"virker ikke"}
            
    except (ValueError,KeyError):
        answer = {"Mistake":"virker ikke"}
    
    answerJson = json.dumps(answer)
    connectionSocket.send(answerJson.encode())
    connectionSocket.close()



serverPort = 16500 
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort))
serverSocket.listen(1) 
print('Server is ready to listen') 

while True: 
    connectionSocket, addr = serverSocket.accept() 
    threading.Thread(target=handleClient, args=(connectionSocket,addr)).start()
