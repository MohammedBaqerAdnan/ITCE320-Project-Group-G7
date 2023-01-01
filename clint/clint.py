import socket , json , tkinter as tk ,time

hostname = '127.0.0.1'
portNumber = 8999

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as cs :
    cs.connect((hostname , portNumber))
    root = tk.Tk(className="Airport")
    root.geometry("1980x1080")
    root.config(bg='#CDCDAD')



    #sending the name and airport NO
    def information():
        name = name_as_string.get()
        icao = icao_as_string.get()
        cs.send(name.encode('ascii'))
        cs.send(icao.encode('ascii'))

    #function of arrival flights
    def arrival_flight() :
        #creating variable a dictionary to send the data with the option number and the value of the search
        choice = {"option":1,"value_search":None}
        choice1 = json.dumps(choice)
        cs.sendall(choice1.encode())
        data = cs.recv(19999)
        data=data.decode()
        data  = json.loads(data)
        move = iter(data)    
        text_box=tk.Text(root , height=23 , width= 72  ,bg= '#8A8A2B',fg= 'black' ,  font=('Arial' , 15))            
        text_box.place(y = 200 , x= 700)  

        while True :                
                try :  
                    
                    text_box.insert(tk.END , 'IATA : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Departure airport : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Arrival time : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Terminal : ' + str(next(move)) + '\n' )                   
                    text_box.insert(tk.END , 'Gate : ' + str(next(move)) + '\n' )
                    text_box.insert(tk.END , 'airport : ' + str(next(move)) + '\n' )
                    
                except StopIteration : 
                    break

        return data


        
    #function of delayed flights            
    def delayed() :
        choice = {"option":2,"value_search":None}
        choice = json.dumps(choice)
        cs.send(choice.encode())
        data = cs.recv(19999)  
        data  = json.loads(data)
        move = iter(data)           
        text_box=tk.Text(root , height=23 , width= 72  ,bg= '##8A8A2B',fg= 'black' ,  font=('Arial' , 15))            
        text_box.place(y = 200 , x= 700)  

        while True :                
                try :  
                    
                    text_box.insert(tk.END , 'IATA : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Departure airport : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Arrival time : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Terminal : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Gate : ' + str(next(move)) + '\n' )
                    text_box.insert(tk.END , 'airport : ' + str(next(move)) + '\n' )
                    
                except StopIteration : 
                    break
        return data


    #function of city information
    def City_info():
        City_name = input("Enter the name of the city you are looking for: ")
        choice = {"option":3,"value_search":City_name}
        choice = json.dumps(choice)
        cs.send(choice.encode())
        data = cs.recv(19999)  
        data  = json.loads(data)
        move = iter(data)            
        text_box=tk.Text(root , height=23 , width= 72  ,bg= '#8A8A2B',fg= 'black' ,  font=('Arial' , 15))            
        text_box.place(y = 200 , x= 700)  

        while True :                
                try :  
                    
                    text_box.insert(tk.END , 'IATA : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Departure airport : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Arrival time : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Terminal : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Gate : ' + str(next(move)) + '\n' )
                    text_box.insert(tk.END , 'airport : ' + str(next(move)) + '\n' )
                                        
                except StopIteration : 
                    break

        return data

    #function of flight details
    def specific_flight(cs):
        flight_NO = input("Enter the flight number: ")   
        choice = {"option":4,"value_search":flight_NO}
        choice = json.dumps(choice)
        cs.send(choice.encode())
        data = cs.recv(19999)  
        data  = json.loads(data)
        move = iter(data)            
        text_box=tk.Text(root , height=23 , width= 72  ,bg= '#8A8A2B',fg= 'black' ,  font=('Arial' , 15))            
        text_box.place(y = 200 , x= 700)  

        while True :                
                try :  
                    
                    text_box.insert(tk.END , 'IATA : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Departure airport : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Arrival time : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Terminal : ' + str(next(move)) + '\n' )                    
                    text_box.insert(tk.END , 'Gate : ' + str(next(move)) + '\n' )
                    text_box.insert(tk.END , 'airport : ' + str(next(move)) + '\n' )
                    
                except StopIteration : 
                    break

        return data

    #function of exit
    def function_exit(cs):
        choice = {"option":'exit',"value_search":None}
        choice = json.dumps(choice)
        cs.send(choice.encode())



    #Enter client name
    Enter_name_label = tk.Label(root , text='ENTER YOUR NAME HERE ', font=('Arrial' , 15 )  , bg='#8A8A2B' , fg='white').place(x= 10 , y = 30   )
    name_as_string  =tk.StringVar()
    Enter_name_entry = tk.Entry(root , textvariable= name_as_string , width=25 , bg='#8A8A2B' , font = "Raleway"   ).place(x= 320 , y= 30  )

    #Enter icao
    Enter_icao_label = tk.Label(root  , text='ENTER AIRPORT CODE (ICAO) ' ,font=('Arrial' , 15) , bg='#8A8A2B' , fg= 'white').place(x =10 , y = 70  )
    icao_as_string = tk.StringVar()
    Enter_icao_entry = tk.Entry(root , textvariable= icao_as_string , width=25 , bg='#8A8A2B' ,font = "Raleway"  ).place(x= 320  ,y = 70 )

    #submit button
    submit_as_string = tk.StringVar()
    submit_button = tk.Button(root , textvariable= submit_as_string  ,command= information , font = "Arial" , bg = '#8A8A2B' , fg='black' , height=1 , width=15).place(x=650  , y = 45) 
    submit_as_string.set('ENTER')


    #Arrival flights
    arrival_as_string = tk.StringVar()
    arrival_button = tk.Button(root  , textvariable = arrival_as_string , command= arrival_flight , font = "Arial " , bg = '#8A8A2B' , fg= 'black' , height= 2 , width= 34 )
    arrival_as_string.set('GET ALL ARRIVED FLIGHTS')
    arrival_button.place(y = 150 , x= 200)


    #Delayed flights
    delayed_as_string= tk.StringVar()
    delayed_button = tk.Button(root  , textvariable = delayed_as_string , command = delayed , font = "Arial" , bg = '#8A8A2B' , fg= 'black' , height= 2 , width= 34 )
    delayed_as_string.set('GET ALL DELAYED FLIGHTS')
    delayed_button.place(y = 250 , x= 200)


    #All flights from specific city
    flights_as_string = tk.StringVar()
    flights_button = tk.Button(root  , textvariable = flights_as_string , command = lambda : main_menu('3')  ,  font = "Arial" , bg = '#8A8A2B' , fg= 'black' , height= 2 , width= 34 )
    flights_as_string.set('Get All Flights Come From Specific City' )
    flights_button.place(y = 350 , x= 200)




    #All data of specefic
    flight_as_string = tk.StringVar()
    fligh_button_entry = tk.Button(root  , textvariable = flight_as_string, command= lambda : main_menu('4'), font = "Arial" , bg = '#8A8A2B' , fg= 'black' , height= 2 , width= 34 )
    flight_as_string.set('Detales Of Specefic')
    fligh_button_entry.place(y = 540 , x= 200)

        


    #quit the program
    quit_as_string = tk.StringVar()
    quit_button = tk.Button(root  , text= 'QUIT THE PROGRAM' , command= quit  , font = "Arial" , bg = '#8A8A2B' , fg= 'black' , height= 2 , width= 34 )
    quit_button.place(y = 710 , x= 200)

    #frame
    fr = tk.Frame(root , bg='#8A8A2B' , highlightbackground="black", highlightthickness=3, height=538 , width=802).place(y = 198 , x= 697)


    #function main menu 
    def main_menu():
        information(cs)

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
                


        def send_option(option) :    
            if option == '3' :
                cs.send('3'.encode('ascii'))
                global Enter_flight_as_string            
                Enter_flight_label = tk.Label(root , text = 'ENTER CITY CODE HERE', font=('Arrial' , 15 )  , bg='#8A8A2B' , fg='white').place(x= 200 , y = 440   )        
                Enter_flight_as_string =tk.StringVar()                
                city_code_entry = tk.Entry(root , textvariable= Enter_flight_as_string , width=10, bg='#8A8A2B' , font = "Arial"  ).place(x= 200 , y= 480  )
                button_as_string = tk.StringVar()                
                city_code_button = tk.Button(root , textvariable= button_as_string , command=City_info, font = "Arial" , bg = '#8A8A2B' , fg='black' , height=1 , width=15).place(x=370  , y = 480)                 
                button_as_string.set('ENTER')
            
            elif option == '4' :                
                global Enter_flights_as_string
                cs.send('4'.encode('ascii'))            
                Enter_flight_label= tk.Label(root , text='ENTER FLIGHT CODE (ICAO)', font=('Arrial' , 15 )  , bg='#8A8A2B' , fg='white').place(x= 200 , y = 620   )                
                Enter_flights_as_string  =tk.StringVar()                
                Enter_slight_entry = tk.Entry(root , textvariable= Enter_flights_as_string , width=10 , bg='#8A8A2B' , font = "Arial"  ).place(x= 200 , y= 660  )
                flight_button_as_string = tk.StringVar()                
                submit_city = tk.Button(root , textvariable= flight_button_as_string  , command= specific_flight , font = "Arial" , bg = '#8A8A2B' , fg='black' , height=1 , width=15).place(x=370  , y = 660)                 
                flight_button_as_string.set('ENTER')
                

    root.mainloop()    
    main_menu()