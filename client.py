#!/usr/bin/python

import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.134.4.1', 5150)
LOOP = True

try:
	while LOOP:
		message = raw_input('msg:')
		
		if message == "q":
			LOOP = False
			
		# Send data
		print >>sys.stderr, 'sending "%s"' % message
		sent = sock.sendto(message, server_address)

		# Receive response
		print >>sys.stderr, 'waiting to receive'
		data, server = sock.recvfrom(4096)
		print >>sys.stderr, 'received "%s"' % data

finally:
	print >>sys.stderr, 'closing socket'
	sock.close()
