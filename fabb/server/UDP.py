#!/usr/bin/python

import socket
import sys
import time

class UDPServer(object):
	
	DEBUG = False
	token = 0
	sessiontime = 0
	
	def __init__(self, address, port=5150): 
		self.address = address
		self.port = port
		msg = self.address + ':' + str(self.port)
		print(msg)
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		# Bind the socket to the port
		server_address = (self.address, self.port)
		if self.DEBUG: 
			print >>sys.stderr, 'starting up on %s port %s' % server_address
		
		self.sock.bind(server_address)
		
		if self.DEBUG: 
			print >>sys.stderr, '\nwaiting to receive message'
		
		self.LOOP = True
	
	def setMouse(self, mouse):
		self.mouse = mouse

	def start(self):
		while self.LOOP:
			data, address = self.sock.recvfrom(4096)	
			
			if len(data) == 0:
				data = '?'
			
			if len(data) >= 1:
				cmd = data[0]
				if cmd == 'q':
					self.stop()
					
				elif cmd == 'c':
					self.click(data)
					
				elif cmd == 'm':
					self.move(data)
                                
				elif cmd == 't':
					#il client richiede token
					self.token()
				elif cmd == 'x':
					#il client annulla la sessione
					self.closeSession()
				
			if data:
				sent = self.sock.sendto(data, address)
	def token(self):
		#self.token = self.token + 1
		self.sessiontime = self.millis()
		#msg = str(self.token) + ' ' + str(self.sessiontime)
		print(str(round(int(time.time())))) 

	def closeSession(self):
		self.sessiontime = 0
				
	def stop(self):
		self.LOOP = False
		if self.DEBUG: 
			print >>sys.stderr, "quit"
	
	def click(self, data):
		if self.DEBUG: 
			print >>sys.stderr, "click"
		self.mouse.click()
	
	def move(self, data):
		buff = ((data.split(":"))[1]).split(",");
		mx = buff[0]
		my = buff[1]
		if self.DEBUG: 
			print >>sys.stderr, "move"
		self.mouse.rmove(mx, my)
	
	def millis(self):
		return int(round(time.time() * 1000))
				
if __name__ == '__main__':
	if self.DEBUG: 
		print ("module UDPServer")
