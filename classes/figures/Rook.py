import pygame

from classes.Figure import Figure

class Rook(Figure):
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		super().__init__(pos, color, board)

		img_path = 'imgs/' + color[0] + '_rook.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 20, board.square_height - 20))

		self.notation = 'R'


	def getPossibleMoves(self, board):
		'''get possible moves of figure'''
		output = []

		moves_north = [] # north
		for y in range(self.y)[::-1]:
			moves_north.append(board.getSquareFromPos((self.x, y)))
		output.append(moves_north)

		moves_east = [] # east
		for x in range(self.x + 1, 8):
			moves_east.append(board.getSquareFromPos((x, self.y)))
		output.append(moves_east)

		moves_south = [] # south
		for y in range(self.y + 1, 8):
			moves_south.append(board.getSquareFromPos((self.x, y)))
		output.append(moves_south)

		moves_west = [] # west
		for x in range(self.x)[::-1]:
			moves_west.append(board.getSquareFromPos((x, self.y)))
		output.append(moves_west)

		return output