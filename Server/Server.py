import json,threading,socket,requests

#main function with try and except and create a thread to handle the client
def main():
    try:
        # Accept a connection
        (active_socket, client_address) = accept_connection(s)
        #create a thread to handle the client
        t=threading.Thread(target=handle_client_request,args=(active_socket,client_address))
        t.start()
    except Exception as e:
        print(e)
        return False

#function to retrieve flight information
def flight_info(airport_code):
    key='758fff0b507ff10b8b758af057976ab6'
    parameter={'access_key':key,'limit':100,'arr_icao':airport_code}
    response=requests.get('http://api.aviationstack.com/v1/flights',parameter)
    response=response.json()
    return response

#function Store the all flight information data in a json file
def store_flight_info(flight_info):
    #open the json file
    with open('group_7.json','w') as file:
        #store the flight information in json file
        json.dump(flight_info,file,indent=2)

#function to store the flight arrive (flight information: flight number and estimated time of arrival and  terminal number) in json object 
def arrive_flight_info(flight_info):
    flight_arrive_info={'IATA':[],'Number':[],'estimated':[],'terminal':[],'gate':[],'airport':[]}
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is arrived
        if flight['flight_status']=='arrived':
            #store the flight information in json object
            flight_arrive_info['IATA'].append(flight['flight']['iata'])
            flight_arrive_info['Number'].append(flight['flight']['number'])
            flight_arrive_info['estimated'].append(flight['arrival']['estimated'])
            flight_arrive_info['terminal'].append(flight['arrival']['terminal'])
            flight_arrive_info['gate'].append(flight['arrival']['delay'])
            flight_arrive_info['airport'].append(flight['departure']['airport'])
    return flight_arrive_info



#function to store the delayed flight (flight information: flight number and estimated time of arrival and  terminal number) in json object 
def delayed_flight_info(flight_info):
    flight_delayed_info={'IATA':[],'Number':[],'estimated':[],'terminal':[],'gate':[],'airport':[]}
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is delayed
        if flight['flight_status']=='delayed':
            #store the flight information in json object
            flight_delayed_info['IATA'].append(flight['flight']['iata'])
            flight_delayed_info['Number'].append(flight['flight']['number'])
            flight_delayed_info['estimated'].append(flight['arrival']['estimated'])
            flight_delayed_info['terminal'].append(flight['arrival']['terminal'])
            flight_delayed_info['gate'].append(flight['arrival']['delay'])
            flight_delayed_info['airport'].append(flight['departure']['airport'])
    return flight_delayed_info

#function to store the for specific city  flights  (flight information: flight number and original time of arrival and  status) in json object 
def city_flight_info(flight_info,city):
    flight_city_info={'IATA':[],'Number':[],'scheduled':[],'terminal':[],'gate':[],'flight_status':[],'airport':[]}
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is arrived
        if flight['arrival']['airport']==city:
            #store the flight information in json object
            flight_city_info['IATA'].append(flight['flight']['iata'])
            flight_city_info['Number'].append(flight['flight']['number'])
            flight_city_info['scheduled'].append(flight['arrival']['scheduled'])
            flight_city_info['terminal'].append(flight['arrival']['terminal'])
            flight_city_info['gate'].append(flight['arrival']['gate'])
            flight_city_info['flight_status'].append(flight['flight_status'])
            flight_city_info['airport'].append(flight['departure']['airport'])
    return flight_city_info

#function to store all details about particular flight  (flight information: flight number and original time of arrival and  status and  estimated time and  terminal number)
#in json object 
def flight_details(flight_info,flight_number):
    flight_city_info={'IATA':[],'Number':[],'scheduled':[],'terminal':[],'gate':[],'flight_status':[],'airport':[],'estimated':[],'DATE':[],'departure_gate':[],'departure_terminal':[],'arrival_airport':[],'arrival_gate':[],'departure_time':[],'Number_departure':[],'delay':[]}
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is arrived
        if flight['flight']['number']==flight_number:
            #store the flight information in json object
            flight_city_info['IATA'].append(flight['flight']['iata'])
            flight_city_info['Number'].append(flight['flight']['number'])
            flight_city_info['scheduled'].append(flight['arrival']['scheduled'])
            flight_city_info['terminal'].append(flight['arrival']['terminal'])
            flight_city_info['gate'].append(flight['arrival']['gate'])
            flight_city_info['flight_status'].append(flight['flight_status'])
            flight_city_info['airport'].append(flight['departure']['airport'])
            flight_city_info['estimated'].append(flight['arrival']['estimated'])
            flight_city_info['DATE'].append(flight['flight_date'])
            flight_city_info['departure_gate'].append(flight['departure']['gate'])
            flight_city_info['departure_terminal'].append(flight['departure']['terminal'])
            flight_city_info['arrival_airport'].append(flight['arrival']['airport'])
            flight_city_info['arrival_gate'].append(flight['arrival']['gate'])
            flight_city_info['departure_time'].append(flight['departure']['scheduled'])
            flight_city_info['Number_departure'].append(flight['departure']['iata'])
            flight_city_info['delay'].append(flight['arrival']['delay'])
    return flight_city_info

#function search if the option is 1 or 2 or 3 or 4 then call the function to store the flight information in json object
def search_flight(option,value_search,flight_info):

    if option=='1':
        re_flight_info=arrive_flight_info(flight_info)
    elif option=='2':
        re_flight_info=delayed_flight_info(flight_info)
    elif option=='3':
        re_flight_info=city_flight_info(flight_info,value_search)
    elif option=='4':
        return_flight_info=flight_details(flight_info,value_search)
    return re_flight_info

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
        #receive the airport code from the client
        airport_code=active_socket.recv(1024).decode()
        #call the function to get the flight information from the airport code
        flight_info=flight_info(airport_code)
        #call the function store the flight information in json file
        store_flight_info(flight_info)
        while True:
            # Receive the client's option with value_search in json object
            client_option = active_socket.recv(1024).decode()
            #convert the json object to python dictionary
            client_option=json.loads(client_option)
            #if the client enter exit option then break the loop
            if client_option['option']=='exit':
                break
            #call the function to search the flight information
            flight_info=search_flight(client_option['option'],client_option['value_search'],flight_info)
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
