import socket , json , tkinter ,time

#creating the socket
#port=8999
#function for connecting to the server 


def connect_to_server():
    #creating the socket
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connecting to the server
    cs.connect(('127.0.0.1', 8999))
    return cs




#sending the name and airport NO
def information(cs):
    #ask the user to enter his name and the airport NO
    name = input("Enter your name: ")
    airport = input("Enter the airport NO: ")
    cs.send(name.encode())
    cs.send(airport.encode())

#function of arrival flights
def arrival_flight(cs) :
    #creating variable a dictionary to send the data with the option number and the value of the search
    choice = {"option":1,"value_search":None}
    choice = json.dumps(choice)
    cs.sendall(choice.encode())
    data = cs.recv(19999)
    data=data.decode()
    data  = json.loads(data)
    return data

    
#function of delayed flights            
def delayed(cs) :
    choice = {"option":2,"value_search":None}
    choice = json.dumps(choice)
    cs.send(choice.encode())
    data = cs.recv(19999)  
    data  = json.loads(data)
    return data

#function of city information
def City_info(cs):
    City_name = input("Enter the name of the city you are looking for: ")
    choice = {"option":3,"value_search":City_name}
    choice = json.dumps(choice)
    cs.send(choice.encode())
    data = cs.recv(19999)  
    data  = json.loads(data)
    return data

#function of flight details
def specific_flight(cs):
    flight_NO = input("Enter the flight number: ")   
    choice = {"option":4,"value_search":flight_NO}
    choice = json.dumps(choice)
    cs.send(choice.encode())
    data = cs.recv(19999)  
    data  = json.loads(data)
    return data

#function of exit
def function_exit(cs):
    choice = {"option":'exit',"value_search":None}
    choice = json.dumps(choice)
    cs.send(choice.encode())

#function main menu 
def main_menu():
    cs=connect_to_server()
    information(cs)
    #make the client wait 
    print("1- Arrival flights")
    print("2- Delayed flights")
    print("3- City information")
    print("4- Flight details")
    print("5- Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            data=arrival_flight(cs)
        elif choice == '2':
            data=delayed(cs)
        elif choice == '3':
            data=City_info(cs)
        elif choice == '4':
            data=specific_flight(cs)
        elif choice == '5':
            function_exit(cs)
            break
        else:
            print("Invalid choice")
        #print the data type dictionary in nice format with the key and the value for each key and one line for each key and value for user to read it easily
        for key, value in data.items():
            print(key, value, sep=':')
            print("")
            

            


    
main_menu()



        
        