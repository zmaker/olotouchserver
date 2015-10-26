import autopy

class MouseMover(object):
    ww = 0
    hh = 0
    def __init__(self):
        scr = autopy.screen.get_size()
        self.ww = scr[0]
        self.hh = scr[1]
        print scr[0]
        print scr[1]

    def move(self, ax, ay):
                if ax < 0:
                        ax = 0
                if ax >= self.ww:
                        ax = self.ww-1
                if ay < 0:
                        ay = 0
                if ay >= self.hh:
                        ay = self.hh-1
		#print(ax)
                #print(ay)
                autopy.mouse.move(int(ax), int(ay))
                return "Moved"

    def smove(self, ax, ay):
                if ax < 0:
                        ax = 0
                if ax >= self.ww:
                        ax = self.ww-1
                if ay < 0:
                        ay = 0
                if ay >= self.hh:
                        ay = self.hh-1
                autopy.mouse.smooth_move(int(ax), int(ay))
                return "Moved"

    def rmove(self, mx, my):
                pos = autopy.mouse.get_pos()
                ax = pos[0] + int(mx)
                ay = pos[1] + int(my)
                if ax < 0:
                        ax = 0
                if ax >= self.ww:
                        ax = self.ww-1
                if ay < 0:
                        ay = 0
                if ay >= self.hh:
                        ay = self.hh-1
                autopy.mouse.move(ax, ay)
                return "Moved"


    def click(self):
                autopy.mouse.click()
                return "click"
    def rclick(self):
                autopy.mouse.toggle(True, autopy.mouse.RIGHT_BUTTON)
                sleep(.1)
                autopy.mouse.toggle(False, autopy.mouse.RIGHT_BUTTON)
                return "rclick"
    def mclick(self):
                autopy.mouse.toggle(True, autopy.mouse.CENTER_BUTTON)
                time.sleep(.1)
                autopy.mouse.toggle(False, autopy.mouse.CENTER_BUTTON)
                return "mclick"

