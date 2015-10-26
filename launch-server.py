#!/usr/bin/python

from fabb.ControlSystem import ControlSystem
from fabb.server.UDP import UDPServer 
from fabb.mouse.MouseMover import MouseMover

'''
lancia il server UDP - stand-alone
'''

if __name__ == "__main__":
    print ("Starting...")
    mm = MouseMover()
    cs = ControlSystem("192.134.4.1", 5150)
    cs.setMouse(mm)
    cs.start()
    
