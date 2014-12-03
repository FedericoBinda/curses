import curses
import time

"""A small snake game"""

class Snake:
	"""A snake is defined by its pixels and direction"""
	def __init__(self):
		self.direction = [0,1] # first element = up +1 or down -1; second = right +1 left -1
		self.pixels = [[0,0]] # the head of the snake is pixellist[0]
	def init_pixels(self,height,width):
		"""initialize the pixels according to the height and width of the window"""
		myrange = range(5)
		myrange.reverse()
		self.pixels = [ [height/2,width/2-i] for i in myrange]
	def show(self,win):
		"""show the snake in the window"""
		win.erase()
		for pixel in self.pixels:
			win.addstr(pixel[0],pixel[1],'x')
	def move(self):
		"""move the snake according to its direction"""
		self.pixels.pop()
		ynew = self.pixels[-1][0] - self.direction[0]
		xnew = self.pixels[-1][1] + self.direction[1]
		self.pixels.insert(0,[ynew,xnew])
	def set_direction(self,dir):
		"""set direction of movement of the snake"""
		self.direction = dir
	def am_i_inside(self,height,width):
		"""check if the snake hit the wall"""
		myposition = self.pixels[0]
		if myposition[0] < 1 or myposition[0] >= height:
			return False
		elif myposition[1] < 1 or myposition[1] >= width:
			return False
		else:
			return True

def mycurse(stdscr):
	curses.curs_set(0) # set invisible cursor
	begin_x = 20 
	begin_y = 7
	height = 10
	width = 40
	win = curses.newwin(height, width, begin_y, begin_x) # init window
	win.nodelay(1) # getch does not block the program
	snake = Snake()
	snake.init_pixels(height,width) # init the snake
	snake.show(win) #show the snake
	time.sleep(1)
	key = ''
	while key != ord('q') and snake.am_i_inside(height,width):
		key = win.getch()
		snake.move()
		snake.show(win)
		time.sleep(1)
	
if __name__ == '__main__':
	curses.wrapper(mycurse)
