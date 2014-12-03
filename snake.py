import curses
import time

"""A small snake game"""

mydirection = 1 # 0 = up, 1 = right, 2 = down, 3 = left
myposition = [1,1]
mylength = 5 # length of the snake

def mycurse(stdscr):
	global myposition
	curses.curs_set(0) # set invisible cursor
	begin_x = 20 
	begin_y = 7
	height = 10
	width = 40
	win = curses.newwin(height, width, begin_y, begin_x) # init window
	myposition = [height/2, width/2] # start snake in the middle
	move(win)
	move(win)
	move(win)
	time.sleep(5)
	
def move(win,dt=1):
	"""move the snake"""
	global myposition
	myposition[1] += 1 # change position (1 to right -> implement direction)
	win.erase() # clear screen
	win.addstr(myposition[0],myposition[1] - mylength,'x'*mylength) # draw snake
	win.refresh()
	time.sleep(dt)

	
if __name__ == '__main__':
	curses.wrapper(mycurse)
