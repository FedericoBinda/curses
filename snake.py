import curses
import time
from numpy import random

"""A small snake game"""

score = 0

class Snake:
	"""A snake is defined by its pixels and direction"""
	def __init__(self,height,width):
		self.direction = 103 # 114 = up (r), 102 = down (f), 103 = right (g), 100 = left (d)
		self.pixels = [[0,0]] # the head of the snake is pixellist[0]
		self.acceptkeys = {114 : [1,0], 102 : [-1,0], 103 : [0,1], 100 : [0,-1]}
		self.length = 5
		self.height = height
		self.width = width
		self.fruit = [5,5]
		self.myscore = 0
		self.init_pixels()
	def init_pixels(self):
		"""initialize the pixels according to the height and width of the window"""
		myrange = range(self.length)
		myrange.reverse()
		self.pixels = [ [self.height/2,self.width/2 - self.length + i] for i in myrange]
	def create_fruit(self):
		"""create a new fruit"""
		self.fruit = [random.randint(2,self.width-1), random.randint(2,self.height-1)]
	def show(self,win):
		"""show the snake in the window"""
		win.erase()
		# display box
		# -----------
		height,width = win.getmaxyx()
		win.hline(0,0,'-',width-1)
		win.hline(height-1,0,'-',width-1)
		win.vline(0,0,'|',height-1)
		win.vline(0,width-1,'|',height-1)
		# display score
		# -------------
		win.addstr(0,width/2,str(self.myscore))
		# display fruit
		# -------------
		x=self.fruit[0]
		y=self.fruit[1]
		win.addstr(y,x,'o')
		# display snake
		# -------------
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
			
	def am_i_inside(self):
		"""check if the snake hit the wall"""
		myposition = self.pixels[0]
		if myposition[0] <= 1 or myposition[0] >= self.height-1:
			return False
		elif myposition[1] <= 1 or myposition[1] >= self.width-1:
			return False
		else:
			return True
			
	def am_i_suicidal(self):
		"""check if the snake killed himself"""
		mylist = [x[0]*1000 + x[1] for x in self.pixels] # horrible trick to check if there are duplicates in pixels
		if len(set(mylist)) < self.length:
			return True
		else:
			return False

	def am_i_eating(self):
		"""check if the snake eats fruit"""
		myposition = self.pixels[0]
		if myposition[0] == self.fruit[1] and myposition[1] == self.fruit[0]:
			self.create_fruit()
			self.myscore += 1
			global score 
			score += 1
			self.length += 1
			self.pixels.append([self.pixels[-1][0] - 1,self.pixels[-1][1]])
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
	snake = Snake(height,width) #init the snake
	snake.show(win) #show the snake
	key = ''
	while key != ord('q') and snake.am_i_inside() and not snake.am_i_suicidal():
		snake.am_i_eating()
		key = win.getch()
		snake.move(key)
		snake.show(win)
		time.sleep(4./(15+snake.myscore))
	
if __name__ == '__main__':
	curses.wrapper(mycurse)
	print 'Your final score was', score
