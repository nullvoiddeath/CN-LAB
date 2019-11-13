import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.124.6.41"
port = 1337

sock.bind((host, port))
sock.listen(1)
print('Server listening!...')
while 1:
	conn, addr = sock.accept()
	print("Got Connection from: " + str(addr))
	data = conn.recv(1024)
	print('Server received: ' + str(repr(data)))
	fname = data
	f = open(fname, 'rb')
	l = f.read(1024)
	while(l):
		conn.send(l)
		#print('Sent ', repr(l))
		l = f.read(1024)
	f.close()

	print('Sent!')
	conn.send('Thanks for connecting. ~Void')
	conn.close()
