import curses
import time
from numpy import random

"""A small snake game"""

class Snake:
	"""A snake is defined by its pixels and direction"""
	def __init__(self):
		self.direction = 103 # 114 = up (r), 102 = down (f), 103 = right (g), 100 = left (d)
		self.pixels = [[0,0]] # the head of the snake is pixellist[0]
		self.acceptkeys = {114 : [1,0], 102 : [-1,0], 103 : [0,1], 100 : [0,-1]}
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
			
	def am_i_suicidal(self):
		"""check if the snake killed himself"""
		mylist = [x[0]*1000 + x[1] for x in self.pixels] # horrible trick to check if there are duplicates in pixels
		if len(set(mylist)) < 5:
			return True
		else:
			return False

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
	while key != ord('q') and snake.am_i_inside(height,width) and not snake.am_i_suicidal():
		key = win.getch()
		snake.move(key)
		snake.show(win)
		time.sleep(0.3)
	
if __name__ == '__main__':
	curses.wrapper(mycurse)
