import curses
import time
from numpy import random

"""A small snake game"""

class Snake:
	"""A snake is defined by its pixels and direction"""
	def __init__(self):
		self.direction = -12 # -14 = up (r), -12 = down (f), -13 = right (g), -10 = left (d)
		self.pixels = [[0,0]] # the head of the snake is pixellist[0]
		self.acceptkeys = {-14 : [1,0], -12 : [-1,0], -13 : [0,1], -10 : [0,-1]}
	def init_pixels(self,height,width):
		"""initialize the pixels according to the height and width of the window"""
		myrange = range(5)
		myrange.reverse()
		self.pixels = [ [height/2,width/2 -5 + i] for i in myrange]
	def show(self,win):
		"""show the snake in the window"""
		win.erase()
		for pixel in self.pixels:
			win.addstr(pixel[0],pixel[1],'x')
		win.refresh()
	def move(self,key):
		"""move the snake according to its direction"""
		self.set_direction(key)
		self.pixels.pop()
		ynew = self.pixels[0][0] - self.acceptkeys[self.direction][0]
		xnew = self.pixels[0][1] + self.acceptkeys[self.direction][1]
		self.pixels.insert(0,[ynew,xnew])
	def set_direction(self,key):
		"""set direction of movement of the snake"""
		if key in self.acceptkeys:
			if self.acceptkeys[key][0] + self.acceptkeys[self.direction][0] != 0: # do not invert direction of motion
				self.direction = key
			
	def am_i_inside(self,height,width):
		"""check if the snake hit the wall"""
		myposition = self.pixels[0]
		if myposition[0] <= 1 or myposition[0] >= height-1:
			return False
		elif myposition[1] <= 1 or myposition[1] >= width-1:
			return False
		else:
			return True

def mycurse(stdscr):
	curses.curs_set(0) # set invisible cursor
	begin_x = 20 
	begin_y = 7
	height = 20
	width = 40
	win = curses.newwin(height, width, begin_y, begin_x) # init window
	win.nodelay(1) # getch() does not block the program
	snake = Snake()
	snake.init_pixels(height,width) # init the snake
	snake.show(win) #show the snake
	key = ''
	while key != ord('q') and snake.am_i_inside(height,width):
		key = win.getch()
		myarg = random.randint(-14,-9)
		snake.move(myarg)
		#win.addstr(1,1,str(key))
		#win.refresh()
		snake.show(win)
		time.sleep(0.2)
	
if __name__ == '__main__':
	curses.wrapper(mycurse)
