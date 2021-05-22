import socket
import pickle

#Class in charge of creating the client side of socket communication
#Establish the communication with the server (cooker)
class client(object):
    def __init__(self, master, **kwargs):
        print("3")

    #place your own ip
    def client_socket(self,z):
        s = socket.socket()
        port = 3125  #insert Port that you want to use, need to be >1024
        ip = '192.168.1.6' #insert server ip
        s.connect((ip, port))
        print(s.getsockname()[1])
        s.sendall(pickle.dumps(z))
        s.close()