import socket , json , tkinter

#creating the socket
#port=8999
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as cs:
    cs.connect(("127.0.0.1" , 8999))

    #creating a top level window
    top = tkinter.Tk()
    top.mainloop()


    
    #sending the name and airport NO
    def information():
        #ask the user to enter his name and the airport NO
        name = input("Enter your name: ")
        airport = input("Enter the airport NO: ")
        cs.send(name.encode())
        cs.send(airport.encode())

    #function of arrival flights
    def arrival_flight() :
        #creating variable a dictionary to send the data with the option number and the value of the search
        choice = {"option":'1',"value_search":None}
        choice = json.dumps(choice)
        cs.send(choice.encode())
        data , address = cs.recv(19999)   
        d = json.loads(data)
    
        
    #function of delayed flights            
    def delayed() :
        choice = {"option":'2',"value_search":None}
        choice = json.dumps(choice)
        cs.send(choice.encode())
        data , address = cs.recv(19999)   
        d = json.loads(data)

    #function of city information
    def City_info():
        City_name = input("Enter the name of the city you are looking for: ")
        choice = {"option":'3',"value_search":City_name}
        choice = json.dumps(choice)
        cs.send(choice.encode())
        data = cs.recv(19999)            
        d  = json.loads(data)

    #function of flight details
    def specific_flight():
        flight_NO = input("Enter the flight number: ")   
        choice = {"option":'4',"value_search":flight_NO}
        choice = json.dumps(choice)
        cs.send(choice.encode())
        data = cs.recv(19999)  
        d  = json.loads(data)



        
        