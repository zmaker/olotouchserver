#!/usr/bin/python

import socket
import sys
import Pyro4

if __name__ == '__main__':
	
	mouse_mover = Pyro4.Proxy("PYRONAME:mouse.mover") 

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Bind the socket to the port
	server_address = ('192.168.3.1', 5150)
	print >>sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	LOOP = True
	while LOOP:
		#print >>sys.stderr, '\nwaiting to receive message'
		data, address = sock.recvfrom(4096)	
		
		#print 'msg: %s' % (data)
		
		if len(data) >= 1:
			cmd = data[0]
			if cmd == 'q':
				LOOP = False
			elif cmd == 'c':
				#print("click")
				mouse_mover.click()
			elif cmd == 'm':
				buff = ((data.split(":"))[1]).split(",");
				mx = buff[0]
				my = buff[1]
				#print("move")
				mouse_mover.rmove(mx, my)
			
		#print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
		#print >>sys.stderr, data
		
		if data:
			sent = sock.sendto(data, address)
			#print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
