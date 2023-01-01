import json,threading,socket,requests,sys

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
    key='a499d3ebda4cd62efd7841c09e4e43bf'
    parameter={'access_key':key,'limit':100}
    response={
  "pagination": {
    "limit": 10,
    "offset": 0,
    "count": 10,
    "total": 544
  },
  "data": [
    {
      "flight_date": "2023-01-01",
      "flight_status": "landed",
      "departure": {
        "airport": "Nanjing Lukou International Airport",
        "timezone": "Asia/Shanghai",
        "iata": "NKG",
        "icao": "ZSNJ",
        "terminal": 'null',
        "gate": 'null',
        "delay": 'null',
        "scheduled": "2023-01-01T01:00:00+00:00",
        "estimated": "2023-01-01T01:00:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": 'null',
        "gate": 'null',
        "baggage": 'null',
        "delay": 1,
        "scheduled": "2022-12-31T17:30:00+00:00",
        "estimated": "2022-12-31T17:30:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "Suparna Airlines",
        "iata": "Y8",
        "icao": "YZR"
      },
      "flight": {
        "number": "7453",
        "iata": "Y87453",
        "icao": "YZR7453",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    },
    {
      "flight_date": "2023-01-01",
      "flight_status": "scheduled",
      "departure": {
        "airport": "Seoul (Incheon)",
        "timezone": "Asia/Seoul",
        "iata": "ICN",
        "icao": "RKSI",
        "terminal": 'null',
        "gate": 'null',
        "delay": 'null',
        "scheduled": "2023-01-01T00:05:00+00:00",
        "estimated": "2023-01-01T00:05:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": 'null',
        "gate": 'null',
        "baggage": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T14:05:00+00:00",
        "estimated": "2022-12-31T14:05:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "Amerijet International",
        "iata": "M6",
        "icao": "AJT"
      },
      "flight": {
        "number": "1010",
        "iata": "M61010",
        "icao": "AJT1010",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    },
    {
      "flight_date": "2023-01-01",
      "flight_status": "scheduled",
      "departure": {
        "airport": "Shanghai Pudong International",
        "timezone": "Asia/Shanghai",
        "iata": "PVG",
        "icao": "ZSPD",
        "terminal": 'null',
        "gate": 'null',
        "delay": 10,
        "scheduled": "2023-01-01T00:25:00+00:00",
        "estimated": "2023-01-01T00:25:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": 'null',
        "gate": 'null',
        "baggage": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T16:55:00+00:00",
        "estimated": "2022-12-31T16:55:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "China Southern Airlines",
        "iata": "CZ",
        "icao": "CSN"
      },
      "flight": {
        "number": "435",
        "iata": "CZ435",
        "icao": "CSN435",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    },
    {
      "flight_date": "2022-12-31",
      "flight_status": "scheduled",
      "departure": {
        "airport": "Shanghai Pudong International",
        "timezone": "Asia/Shanghai",
        "iata": "PVG",
        "icao": "ZSPD",
        "terminal": 'null',
        "gate": 'null',
        "delay": 77,
        "scheduled": "2022-12-31T08:35:00+00:00",
        "estimated": "2022-12-31T08:35:00+00:00",
        "actual": "2022-12-31T09:51:00+00:00",
        "estimated_runway": "2022-12-31T09:51:00+00:00",
        "actual_runway": "2022-12-31T09:51:00+00:00"
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": "S",
        "gate": 'null',
        "baggage": 'null',
        "delay": 46,
        "scheduled": "2022-12-31T01:00:00+00:00",
        "estimated": "2022-12-31T01:00:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "China Cargo",
        "iata": "CK",
        "icao": "CKK"
      },
      "flight": {
        "number": "227",
        "iata": "CK227",
        "icao": "CKK227",
        "codeshared": 'null'
      },
      "aircraft": {
        "registration": "B-221S",
        "iata": "B77L",
        "icao": "B77L",
        "icao24": "781D6D"
      },
      "live": {
        "updated": "2022-12-31T03:21:10+00:00",
        "latitude": 33.79,
        "longitude": 138.65,
        "altitude": 9448.8,
        "direction": 67,
        "speed_horizontal": 1227.88,
        "speed_vertical": 0,
        "is_ground": False
      }
    },
    {
      "flight_date": "2022-12-31",
      "flight_status": "unknown",
      "departure": {
        "airport": "Nanjing Lukou International Airport",
        "timezone": "Asia/Shanghai",
        "iata": "NKG",
        "icao": "ZSNJ",
        "terminal": 'null',
        "gate": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T05:55:00+00:00",
        "estimated": "2022-12-31T05:55:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": "S",
        "gate": 'null',
        "baggage": 'null',
        "delay": 'null',
        "scheduled": "2022-12-30T22:30:00+00:00",
        "estimated": "2022-12-30T22:30:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "Suparna Airlines",
        "iata": "Y8",
        "icao": "YZR"
      },
      "flight": {
        "number": "7451",
        "iata": "Y87451",
        "icao": "YZR7451",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    },
    {
      "flight_date": "2022-12-31",
      "flight_status": "scheduled",
      "departure": {
        "airport": "Taiwan Taoyuan International (Chiang Kai Shek International)",
        "timezone": "Asia/Taipei",
        "iata": "TPE",
        "icao": "RCTP",
        "terminal": 'null',
        "gate": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T14:00:00+00:00",
        "estimated": "2022-12-31T14:00:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": "S",
        "gate": 'null',
        "baggage": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T06:30:00+00:00",
        "estimated": "2022-12-31T06:30:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "China Airlines",
        "iata": "CI",
        "icao": "CAL"
      },
      "flight": {
        "number": "5232",
        "iata": "CI5232",
        "icao": "CAL5232",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    },
    {
      "flight_date": "2022-12-31",
      "flight_status": "active",
      "departure": {
        "airport": "Taiwan Taoyuan International (Chiang Kai Shek International)",
        "timezone": "Asia/Taipei",
        "iata": "TPE",
        "icao": "RCTP",
        "terminal": 'null',
        "gate": 'null',
        "delay": 10,
        "scheduled": "2022-12-31T14:00:00+00:00",
        "estimated": "2022-12-31T14:00:00+00:00",
        "actual": "2022-12-31T13:59:00+00:00",
        "estimated_runway": "2022-12-31T13:59:00+00:00",
        "actual_runway": "2022-12-31T13:59:00+00:00"
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": "S",
        "gate": 'null',
        "baggage": 'null',
        "delay": 31,
        "scheduled": "2022-12-31T05:20:00+00:00",
        "estimated": "2022-12-31T05:20:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "China Airlines",
        "iata": "CI",
        "icao": "CAL"
      },
      "flight": {
        "number": "5240",
        "iata": "CI5240",
        "icao": "CAL5240",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    },
    {
      "flight_date": "2022-12-31",
      "flight_status": "scheduled",
      "departure": {
        "airport": "Shanghai Pudong International",
        "timezone": "Asia/Shanghai",
        "iata": "PVG",
        "icao": "ZSPD",
        "terminal": 'null',
        "gate": 'null',
        "delay": 10,
        "scheduled": "2022-12-31T09:35:00+00:00",
        "estimated": "2022-12-31T09:35:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": "S",
        "gate": 'null',
        "baggage": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T02:00:00+00:00",
        "estimated": "2022-12-31T02:00:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "China Southern Airlines",
        "iata": "CZ",
        "icao": "CSN"
      },
      "flight": {
        "number": "431",
        "iata": "CZ431",
        "icao": "CSN431",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    },
    {
      "flight_date": "2022-12-31",
      "flight_status": "active",
      "departure": {
        "airport": "Xiamen",
        "timezone": "Asia/Shanghai",
        "iata": "XMN",
        "icao": "ZSAM",
        "terminal": 'null',
        "gate": 'null',
        "delay": 11,
        "scheduled": "2022-12-31T13:00:00+00:00",
        "estimated": "2022-12-31T13:00:00+00:00",
        "actual": "2022-12-31T13:11:00+00:00",
        "estimated_runway": "2022-12-31T13:11:00+00:00",
        "actual_runway": "2022-12-31T13:11:00+00:00"
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": "S",
        "gate": 'null',
        "baggage": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T04:45:00+00:00",
        "estimated": "2022-12-31T04:45:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "Sky Lease Cargo",
        "iata": "GG",
        "icao": "KYE"
      },
      "flight": {
        "number": "4874",
        "iata": "GG4874",
        "icao": "KYE4874",
        "codeshared": 'null'
      },
      "aircraft": {
        "registration": "N903AR",
        "iata": "B744",
        "icao": "B744",
        "icao24": "AC7A61"
      },
      "live": {
        "updated": "2022-12-31T09:41:12+00:00",
        "latitude": 49.05,
        "longitude": 158.97,
        "altitude": 9448.8,
        "direction": 47,
        "speed_horizontal": 1031.56,
        "speed_vertical": 0,
        "is_ground": False
      }
    },
    {
      "flight_date": "2022-12-31",
      "flight_status": "scheduled",
      "departure": {
        "airport": "Seoul (Incheon)",
        "timezone": "Asia/Seoul",
        "iata": "ICN",
        "icao": "RKSI",
        "terminal": 'null',
        "gate": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T09:30:00+00:00",
        "estimated": "2022-12-31T09:30:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "arrival": {
        "airport": "Ted Stevens Anchorage International Airport",
        "timezone": "America/Anchorage",
        "iata": "ANC",
        "icao": "PANC",
        "terminal": "S",
        "gate": 'null',
        "baggage": 'null',
        "delay": 'null',
        "scheduled": "2022-12-31T00:30:00+00:00",
        "estimated": "2022-12-31T00:30:00+00:00",
        "actual": 'null',
        "estimated_runway": 'null',
        "actual_runway": 'null'
      },
      "airline": {
        "name": "Polar Air Cargo",
        "iata": "PO",
        "icao": "PAC"
      },
      "flight": {
        "number": "938",
        "iata": "PO938",
        "icao": "PAC938",
        "codeshared": 'null'
      },
      "aircraft": 'null',
      "live": 'null'
    }
  ]
}
    return response

#function Store the all flight information data in a json file
def store_flight_info(flight_info):
    #open the json file
    with open('group_test.json','w') as file:
        #store the flight information in json file
        json.dump(flight_info,file,indent=2)

#function to store the flight arrive (flight information: flight number and estimated time of arrival and  terminal number) in json object 
def arrive_flight_info(flight_info):
    flight_arrive_info={'IATA':[],'Number':[],'estimated':[],'terminal':[],'gate':[],'airport':[]}
    #loop through the flight information
    for flight in flight_info['data']:
        #if the flight is arrived
        if flight['flight_status']=='landed':
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
        if flight['arrival']['delay']!='null':
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
        if flight['departure']['iata']==city:
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
        if flight['flight']['icao']==flight_number:
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
    #re_flight_info equal to null not prevent the error
    re_flight_info={'IATA':[],'Number':[],'scheduled':[],'terminal':[],'gate':[],'flight_status':[],'airport':[],'estimated':[],'DATE':[],'departure_gate':[],'departure_terminal':[],'arrival_airport':[],'arrival_gate':[],'departure_time':[],'Number_departure':[],'delay':[]}
    if option==1:
        re_flight_info=arrive_flight_info(flight_info)
    elif option==2:
        re_flight_info=delayed_flight_info(flight_info)
    elif option==3:
        re_flight_info=city_flight_info(flight_info,value_search)
    elif option==4:
        re_flight_info=flight_details(flight_info,value_search)
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
        flight_info_i=flight_info(airport_code)
        #call the function store the flight information in json file
        store_flight_info(flight_info_i)
        while True:
            # Receive the client's option with value_search in json object
            client_option = active_socket.recv(1024).decode()
            #convert the json object to python dictionary
            client_option=json.loads(client_option)
            #if the client enter exit option then break the loop
            if client_option['option']=='exit':
                break
            #call the function to search the flight information
            flight_info_in=search_flight(client_option['option'],client_option['value_search'],flight_info_i)
            #convert the flight information to json object  to send it to the client
            flight_info_in=json.dumps(flight_info_in)
            # Send the flight information to the client
            active_socket.sendall(flight_info_in.encode())
        # Display the client's name and id with the message "has disconnected"
        print(f'client {client_name} with id {id_number} has been disconnected')
        #remove the client from the online clients list
        online_clients.remove(client_info)
    except Exception as e:
        #print the error message
        print(e)
        #print the error line number
        print(sys.exc_info()[-1].tb_lineno)

        print(f'client {client_name} with id {id_number} has been disconnected')
        #remove the client from the online clients list
        online_clients.remove(client_info)




#function to create a passive socket
def create_passive_socket(listen_backlog):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a port
    s.bind(('127.0.0.1', 8999))
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
if __name__ == '__main__':
    while True:
        #if the main function return false break the loop
        if main()==False:
            break

#close socket
s.close()
