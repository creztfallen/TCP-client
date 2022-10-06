import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM,
                          0)
    except socket.error as err:
        print("Connection failed!")
        print("Error: {}".format(err))
        sys.exit()
        
    print("Socket successfully created.")        
    
    Host = input("Type the Host or Ip to be connected: ")
    Port = input("Type the Port to be connected: ")
    

    try:
        s.connect((Host, int(Port)))
        print("TCP Client successfully connected on Host:" + Host + " on Port " + Port)
        s.shutdown(2)
    except socket.error as err:
        print("Impossible to connect to the Host: " + Host + " -- Port: " + Port)
        print("Error: {}".format(err))
        sys.exit()
        
if __name__ == "__main__":
    main()