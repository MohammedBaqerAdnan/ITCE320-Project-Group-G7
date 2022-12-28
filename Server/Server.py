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

#function to store all details about particular flight  (flight information: flight number and original time of arrival and  status and  estimated time and  terminal number) in json object 
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
