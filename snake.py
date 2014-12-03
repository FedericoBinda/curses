import curses
import time

"""A small snake game"""

mydirection = 1 # 0 = up, 1 = right, 2 = down, 3 = left
myposition = [1,1] # y,x
mylength = 5 # length of the snake

def am_i_inside(height,width):
	"""check if the snake hit the wall"""
	if myposition[0] < 1 or myposition[0] >= height:
		return False
	elif myposition[1] < 1 or myposition[1] >= width:
		return False
	else:
		return True

def mycurse(stdscr):
	global myposition
	curses.curs_set(0) # set invisible cursor
	begin_x = 20 
	begin_y = 7
	height = 10
	width = 40
	win = curses.newwin(height, width, begin_y, begin_x) # init window
	win.nodelay(1) # getch does not block the program
	myposition = [height/2, width/2] # start snake in the middle
	key = ''
	while key != ord('q') and am_i_inside(height,width):
		key = win.getch()
		move(win)
	
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
