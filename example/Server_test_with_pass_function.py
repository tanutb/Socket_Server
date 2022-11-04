'''
Pass function as argument

Argument up2u
if u need argument more than one 
u need to add arugument in line 30 in SocketServer.py

'''


from SocketSever import Socket

##Function  
def plus_1_all_list(data):    
    
    print(list(map(lambda x : x+1,data)))


Server = Socket()
Server.echo_server(function=plus_1_all_list)