import socket , json

#creatig the socket
port=8999
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as cs:
        cs.connect(("" , port))
    

        #function of arrival flights
        def arrival_flight() :
            cs.send('1'.encode())
            data , address = cs.recv()   
            d = json.loads(data)
        
         
        #function of delayed flights            
        def delayed() :
            cs.send('2'.encode())
            data , address = cs.recv()   
            d = json.loads(data)
        
        