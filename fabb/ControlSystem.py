#!/usr/bin/python

from server.UDP import UDPServer 
from mouse.MouseMover import MouseMover 

class ControlSystem(object):
	
	def __init__(self, address, port=5150): 
		self.address = address
		self.port = port
		print ("init class")
		
		self.srv = UDPServer(self.address, self.port)
	
	def start(self):
		self.srv.setMouse(self.mouse)
		self.srv.start()
		
	def setMouse(self, mouse):
		self.mouse = mouse

if __name__ == "__main__":
    print ("ControlSystem")
    mm = MouseMover()
    cs = ControlSystem("127.0.0.1", 5150)
    cs.setMouse(mm)
    cs.start()
    #srv = UDPServer()
