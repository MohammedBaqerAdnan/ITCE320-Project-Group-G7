import json,threading,socket,requests

#main function with try and except and create a thread to handle the client
def main():
    try:
        # Accept a connection
        (active_socket, client_address) = accept_connection(s)
        #create a thread to handle the client
        t=threading.Thread(target='',args=(active_socket,client_address))
        t.start()
    except Exception as e:
        print(e)
        return False

#function to retrieve flight information
def flight_info(airport_code):
    key='bac0a8b3e116f33f338701edd40d4ae6'
    parameter={'access_key':key,'limit':100,'arr_icao':airport_code}
    response=requests.get('http://api.aviationstack.com/v1/flights',params=parameter)
    response=response.json()
    return response

#function Store the all flight information data in a json file
def store_flight_info(flight_info):
    #open the json file
    with open('flight_info.json','w') as file:
        #store the flight information in json file
        json.dump(flight_info,file)

#function to store the flight arrive (flight information: flight number and estimated time of arrival and  terminal number) in json object 
def arrive_flight_info(flight_info):
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is arrived
        if flight['flight_status']=='arrived':
            #store the flight information in json object
            flight_arrive_info={
                'IATA':flight['flight']['iata'],
                'Number':flight['flight']['number'],
                'estimated':flight['arrival']['estimated'],
                'terminal':flight['arrival']['estimated'],
                'gate':flight['arrival']['delay'],
                'airport':flight['departure']['airport]'],
            }
    return flight_arrive_info



#function to store the delayed flight (flight information: flight number and estimated time of arrival and  terminal number) in json object 
def delayed_flight_info(flight_info):
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is delayed
        if flight['flight_status']=='delayed':
            #store the flight information in json object
            flight_delayed_info={
                'IATA':flight['flight']['iata'],
                'Number':flight['flight']['number'],
                'estimated':flight['arrival']['estimated'],
                'terminal':flight['arrival']['terminal'],
                'gate':flight['arrival']['delay'],
                'airport':flight['departure']['airport]'],
            }
    return flight_delayed_info

#function to store the for specific city  flights  (flight information: flight number and original time of arrival and  status) in json object 
def city_flight_info(flight_info,city):
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is arrived
        if flight['arrival']['airport']==city:
            #store the flight information in json object
            flight_city_info={
                'IATA':flight['flight']['iata'],
                'Number':flight['flight']['number'],
                'scheduled':flight['arrival']['scheduled'],
                'terminal':flight['arrival']['terminal'],
                'gate':flight['arrival']['gate'],
                'flight_status':flight['flight_status'],
                'airport':flight['departure']['airport]'],
            }
    return flight_city_info

#function to store all details about particular flight  (flight information: flight number and original time of arrival and  status and  estimated time and  terminal number)
 #in json object 
def flight_details(flight_info,flight_number):
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is arrived
        if flight['flight']['number']==flight_number:
            #store the flight information in json object
            flight_details={
                'IATA':flight['flight']['iata'],
                'Number':flight['flight']['number'],
                'scheduled':flight['arrival']['scheduled'],
                'terminal':flight['arrival']['terminal'],
                'gate':flight['arrival']['gate'],
                'flight_status':flight['flight_status'],
                'airport':flight['departure']['airport]'],
                'estimated':flight['arrival']['estimated'],
                'DATE':flight['flight_date'],
                'departure_gate':flight['departure']['gate'],
                'departure_terminal':flight['departure']['terminal'],
                'arrival_airport':flight['arrival']['airport'],
                'arrival_gate':flight['arrival']['gate'],
                'departure_time':flight['departure']['scheduled'],
                'Number':flight['departure']['scheduled'],
                'delay':flight['arrival']['delay'],
            }
    return flight_details

#function search if the option is 1 or 2 or 3 or 4 then call the function to store the flight information in json object
def search_flight(option,value_search):

    if option=='1':
        flight_info=arrive_flight_info(flight_info)
    elif option=='2':
        flight_info=delayed_flight_info(flight_info)
    elif option=='3':
        flight_info=city_flight_info(flight_info,value_search)
    elif option=='4':
        flight_info=flight_details(flight_info,value_search)
    return flight_info

#create a list to store the online clients 
online_clients=[]
#function to handle the client request Wait for clients' requests to connect (should be able to accept three connections simultaneously).Accept the connection and Store the client’s name and display it on the terminal.
def handle_client_request(active_socket,id_number):
    try:
        # Receive the client's name
        client_name = active_socket.recv(1024).decode()
        #create a json object to store the client information his name and id number
        client_info={
            'name':client_name,
            'id':id_number
        }
        online_clients.append(client_info)
        # Display the client's name and id with the message "has connected"
        print(f'client {client_name} with id {id_number} has been connected')
        #receive the client option and value in json object to search in loop until the client enter exit option
        while True:
            # Receive the client's option with value_search in json object
            client_option = active_socket.recv(1024).decode()
            #convert the json object to python dictionary
            client_option=json.loads(client_option)
            #if the client enter exit option then break the loop
            if client_option['option']=='exit':
                break
            #call the function to search the flight information
            flight_info=search_flight(client_option['option'],client_option['value_search'])
            #convert the flight information to json object  to send it to the client
            flight_info=json.dumps(flight_info)
            # Send the flight information to the client
            active_socket.sendall(flight_info.encode())
        # Display the client's name and id with the message "has disconnected"
        print(f'client {client_name} with id {id_number} has been disconnected')
        #remove the client from the online clients list
        online_clients.remove(client_info)
    except:
        print(f'client {client_name} with id {id_number} has been disconnected')
        #remove the client from the online clients list
        online_clients.remove(client_info)




#function to create a passive socket
def create_passive_socket(listen_backlog):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a port
    s.bind(('  ', 8999))
    # Listen for connections
    s.listen(listen_backlog)
    # Return the socket and the port number
    return s

#function to accept a connection
def accept_connection(s):
    # Accept a connection
    (active_socket, client_address) = s.accept()
    # Return the socket and the client address
    return (active_socket, client_address)


# Create a passive socket
s = create_passive_socket(3)

#call the main function in while loop
while True:
    #if the main function return false break the loop
    if main()==False:
        break

#close socket
s.close()
