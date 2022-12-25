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
