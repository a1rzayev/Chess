'''imports required in our file'''
import pygame

class Square:
	''' class Square, which objects are placed on the chessboard

	    functions:
		    __init__
			getCoordinates
			draw

		params:
			x
			y
			width
			height
			abs_x
			abs_y
			abs_pos
			pos
			color
			highlight_color
			occupying_figure
			coord
			highlight'''

	def __init__(self, x, y, width, height):
		'''initializes element of our class. this function also calls constructor'''
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.abs_x = x * width
		self.abs_y = y * height
		self.abs_pos = (self.abs_x, self.abs_y)
		self.pos = (x, y)
		# Red Green Blue
		'''if(dhfjsd):
				ssfgsh
			else:
				sdfshdf'''
		self.color = (255, 255, 255) if (x + y) % 2 == 0 else (128, 128, 128)
		self.highlight_color = (0, 128, 0)
		self.occupying_figure = None
		self.coord = self.getCoordinates()
		self.highlight = False

		self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

	def getCoordinates(self):
		'''returns coordinates of our square [x][y]'''
		columns = 'abcdefgh'
		return columns[self.x] + str(self.y + 1)

	def draw(self, display):
		'''draws our square on the board'''
		if (self.highlight):
			pygame.draw.rect(display, self.highlight_color, self.rect)
		else:
			pygame.draw.rect(display, self.color, self.rect)

		if (self.occupying_figure != None):
			centering_rect = self.occupying_figure.img.get_rect()
			centering_rect.center = self.rect.center
			display.blit(self.occupying_figure.img, centering_rect.topleft)