#!/usr/bin/env python
from __future__ import division
 
import pygtk
pygtk.require('2.0')
import gtk
import os
from time import time
from math import floor
gtk.gdk.threads_init()
import gobject

#import autopy
import threading

from fabb.mouse.MouseMover import MouseMover 
from fabb.server.UDP import UDPServer 
from fabb.ControlSystem import ControlSystem 
        
#Parameters
MIN_WORK_TIME = 60 * 10 # min work time in seconds
 
class Pomodoro:
    t = None
    def __init__(self):
        self.icon=gtk.status_icon_new_from_file(self.icon_directory()+"resources/mouse.png")
        self.icon.set_tooltip("Listening...")
        #self.state = "idle"
        #self.tick_interval=10 #number of seconds between each poll
        #self.icon.connect('activate',self.icon_click)
        self.icon.set_visible(True)
        #self.start_working_time = 0

    def icon_directory(self):
        return os.path.dirname(os.path.realpath(__file__)) + os.path.sep

    def icon_click(self,dummy):
        print("quitting...")       
        gtk.main_quit()
        
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        #source_id = gobject.timeout_add(self.tick_interval, self.update)
        
        gtk.main()
        
        
def startServer():
    #mouse_mover=MouseMover()
    print("starting server...")
    mm = MouseMover()
    cs = ControlSystem("127.0.0.1", 5150)
    cs.setMouse(mm)
    cs.start()
 
# If the program is run directly or passed as an argument to the python
# interpreter then create a Pomodoro instance and show it
if __name__ == "__main__":
    t = threading.Thread(target=startServer)
    t.daemon = False
    t.start()
        
    app = Pomodoro()
    app.main()
    '''
    print ("ControlSystem")
    
    ''' 
