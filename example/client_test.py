from SocketSever import Socket
A = Socket()
A.client_connect()
l = [1,2,3,4]
A.client_send_data(l)