'''import requests , json

params = {
    'access_key': '758fff0b507ff10b8b758af057976ab6',
    'limit' : '2'
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params).json()

dat = json.dumps(api_result)

data = json.loads(dat)

with open('groupe_15.json' , 'w') as file :
    json.dump(api_result , indent= 3 , fp= file ) '''


import requests,json ,sys

flight_info={
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 1669022
    },
    "data": [
        {
            "flight_date": "2019-12-12",
            "flight_status": "active",
            "departure": {
                "airport": "San Francisco International",
                "timezone": "America/Los_Angeles",
                "iata": "SFO",
                "icao": "KSFO",
                "terminal": "2",
                "gate": "D11",
                "delay": 13,
                "scheduled": "2019-12-12T04:20:00+00:00",
                "estimated": "2019-12-12T04:20:00+00:00",
                "actual": "2019-12-12T04:20:13+00:00",
                "estimated_runway": "2019-12-12T04:20:13+00:00",
                "actual_runway": "2019-12-12T04:20:13+00:00"
            },
            "arrival": {
                "airport": "Dallas/Fort Worth International",
                "timezone": "America/Chicago",
                "iata": "DFW",
                "icao": "KDFW",
                "terminal": "A",
                "gate": "A22",
                "baggage": "A17",
                "delay": 0,
                "scheduled": "2019-12-12T04:20:00+00:00",
                "estimated": "2019-12-12T04:20:00+00:00",
                "actual": None,
                "estimated_runway": None,
                "actual_runway": None
            },
            "airline": {
                "name": "American Airlines",
                "iata": "AA",
                "icao": "AAL"
            },
            "flight": {
                "number": "1004",
                "iata": "AA1004",
                "icao": "AAL1004",
                "codeshared": None
            },
            "aircraft": {
               "registration": "N160AN",
               "iata": "A321",
               "icao": "A321",
               "icao24": "A0F1BB"
            },
            "live": {
                "updated": "2019-12-12T10:00:00+00:00",
                "latitude": 36.28560000,
                "longitude": -106.80700000,
                "altitude": 8846.820,
                "direction": 114.340,
                "speed_horizontal": 894.348,
                "speed_vertical": 1.188,
                "is_ground": False
            }
        }, 
    ]
}
#function Store the all flight information data in a json file
def store_flight_info(flight_info):
    #open the json file
    with open('group_7.json','w') as file:
        #store the flight information in json file
        json.dump(flight_info,file,indent=2)

#function search if the option is 1 or 2 or 3 or 4 then call the function to store the flight information in json object
def search_flight(option,value_search,flight_info):

    if option=='1':
        re_flight_info=arrive_flight_info(flight_info)
    elif option=='2':
        re_flight_info=delayed_flight_info(flight_info)
    elif option=='3':
        re_flight_info=city_flight_info(flight_info,value_search)
    elif option=='4':
        re_flight_info=flight_details(flight_info,value_search)
    return re_flight_info

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
        if flight['arrival']['delay']>0:
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

#create a list to store the online clients 
online_clients=[]
#function to handle the client request Wait for clients' requests to connect (should be able to accept three connections simultaneously).Accept the connection and Store the client’s name and display it on the terminal.
def handle_client_request(id_number,client_name,airport_code,client_option):
    try:
        client_info={
            'name':client_name,
            'id':id_number
        }
        online_clients.append(client_info)
        # Display the client's name and id with the message "has connected"
        print(f'client {client_name} with id {id_number} has been connected')
        #call the function store the flight information in json file
        store_flight_info(flight_info)
        while True:
            #if the client enter exit option then break the loop
            if client_option['option']=='exit':
                break
            #call the function to search the flight information
            flight_info_in=search_flight(client_option['option'],client_option['value_search'],flight_info)
            break
        # Display the client's name and id with the message "has disconnected"
        print(flight_info_in)
        print(f'client {client_name} with id {id_number} has been disconnected')
        #remove the client from the online clients list
        online_clients.remove(client_info)
    except Exception as e:
        print(e)
        #diplay the error line number
        print(sys.exc_info()[-1].tb_lineno)
        print(f'client {client_name} with id {id_number} has been disconnected')
        #remove the client from the online clients list
        online_clients.remove(client_info)

handle_client_request(1,'ahmed','CAI',{"option":'2',"value_search":'AAL1004'})
