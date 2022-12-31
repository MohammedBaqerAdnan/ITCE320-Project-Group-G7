import socket
import json
import tkinter

#creatig the socket
#port=8999
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as cs:
        cs.connect(("127.0.0.1" , 8999))

        #creating a top level window
        top = tkinter.Tk()
        top.mainloop()


        
        #sending the name and airport NO
        def information():
            name = input("pleas enter your name")
            airPCode = input("pleas enter the airporrt NO")
            cs.send(name.encode())
            cs.send(airPCode.encde())

        #function of arrival flights
        def arrival_flight() :
            cs.send('1'.encode())
            data , address = cs.recv(19999)   
            d = json.loads(data)
        
         
        #function of delayed flights            
        def delayed() :
            cs.send('2'.encode())
            data , address = cs.recv(19999)   
            d = json.loads(data)

        #function of city informations
        def City_info():
            cs.send('3'.encode())
            City_name = input("pleas enter the name of the city you are looking for: ")
            data = cs.recv(19999)            
            d  = json.loads(data)

        #function of flight details
        def specfic_flight():
            cs.send('4'.encode())  
            flight_NO = input("pleas enter the flight number: ")   
            data = cs.recv(19999)  
            d  = json.loads(data)



        
        