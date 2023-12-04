'''imports required in our file'''
import pygame
from classes.Figure import Figure

class Queen(Figure):
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		super().__init__(pos, color, board)

		img_path = 'imgs/' + color[0] + '_queen.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 20, board.square_height - 20))

		self.notation = 'Q'


	def getPossibleMoves(self, board):
		'''get possible moves of figure'''
		possible_moves = []

		moves_north = [] # north
		for y in range(self.y)[::-1]:
			moves_north.append(board.getSquareFromPos((self.x, y)))
		possible_moves.append(moves_north)

		moves_ne = [] # north-east
		for i in range(1, 8):
			if (self.x + i > 7 or self.y - i < 0):
				break
			moves_ne.append(board.getSquareFromPos((self.x + i, self.y - i)))
		possible_moves.append(moves_ne)

		moves_east = [] # east
		for x in range(self.x + 1, 8):
			moves_east.append(board.getSquareFromPos((x, self.y)))
		possible_moves.append(moves_east)

		moves_se = [] # south-east
		for i in range(1, 8):
			if (self.x + i > 7 or self.y + i > 7):
				break
			moves_se.append(board.getSquareFromPos((self.x + i, self.y + i)))
		possible_moves.append(moves_se)

		moves_south = [] # south
		for y in range(self.y + 1, 8):
			moves_south.append(board.getSquareFromPos((self.x, y)))
		possible_moves.append(moves_south)

		moves_sw = [] # south-west
		for i in range(1, 8):
			if (self.x - i < 0 or self.y + i > 7):
				break
			moves_sw.append(board.getSquareFromPos((self.x - i, self.y + i)))
		possible_moves.append(moves_sw)

		moves_west = [] # west
		for x in range(self.x)[::-1]:
			moves_west.append(board.getSquareFromPos((x, self.y)))
		possible_moves.append(moves_west)

		moves_nw = [] # north-west
		for i in range(1, 8):
			if (self.x - i < 0 or self.y - i < 0):
				break
			moves_nw.append(board.getSquareFromPos((self.x - i, self.y - i)))
		possible_moves.append(moves_nw)

		return possible_moves