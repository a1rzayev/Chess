'''imports required in our file'''
import pygame
from classes.Figure import Figure

class Rook(Figure):
	''' class Rook, which is child class of Figure.
	  	Object contains chess figure Rook.

	    functions:
			(all functions of Figure. Because it's Figure's child elem)
		    __init__
			getPossibleMoves

		params:
			(all parametres of Figure. Because it's Figure's child elem)
			img
			notation'''
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		super().__init__(pos, color, board)

		img_path = 'imgs/' + color[0] + '_rook.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 20, board.square_height - 20))

		self.notation = 'R'


	def getPossibleMoves(self, board):
		'''get possible moves of figure'''
		possible_moves = []

		moves_north = [] # north
		for y in range(self.y)[::-1]:
			moves_north.append(board.getSquareFromPos((self.x, y)))
		possible_moves.append(moves_north)

		moves_east = [] # east
		for x in range(self.x + 1, 8):
			moves_east.append(board.getSquareFromPos((x, self.y)))
		possible_moves.append(moves_east)

		moves_south = [] # south
		for y in range(self.y + 1, 8):
			moves_south.append(board.getSquareFromPos((self.x, y)))
		possible_moves.append(moves_south)

		moves_west = [] # west
		for x in range(self.x)[::-1]:
			moves_west.append(board.getSquareFromPos((x, self.y)))
		possible_moves.append(moves_west)

		return possible_moves