import socket
import pickle
#import time 

class Socket:
    def __init__(self,IP="localhost",PORT=1119) -> None:
        self.HOST_IP = IP
        self.PORT = PORT
        self.feedback = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.first_time = True

    def send_array_data(self,s,array):   
        data=pickle.dumps(array)
        s.send(data)

    ##### FOR SERVER ########
    def echo_server(self,function=print):         #pass function
        self.s.bind((self.HOST_IP,self.PORT))
        self.s.listen()
        print(f"Watting for connect")
        conn, addr = self.s.accept()
        with conn:
            print(f"Connected by {addr}")
            ## starttime = time.time() for timer
            while True:
                rev = conn.recv(1024)
                if rev:
                    data=pickle.loads(rev)
                    ## Funtion Something
                    function(data)

                    '''
                    time.sleep(60.0 - ((time.time() - starttime) % 60.0)) 
                    
                    # this code is update every x seconds
                    # (The code doesn't execute every 60 seconds. 
                    # it puts a 60 second gap between executions. It only happens every 60 seconds if your executed code takes no time at all.
                    # so )

                    # no need to use i think
                    
                    '''
                    conn.sendall(b"PBestkodlnw")
                
                else : 
                    #for didnt get any data from client
                    pass
                
        


    ##### FOR CLIENT ########
    def client_connect(self):
        self.s.connect((self.HOST_IP, self.PORT))

    def client_send_data(self,array):
        self.send_array_data(self.s,array)
        self.s.recv(1024)






        
