'''imports required in our file'''
import pygame
from classes.Figure import Figure

class Pawn(Figure):
	''' class Pawn, which is child class of Figure.
	  	Object contains chess figure Pawn.

	    functions:
			(all functions of Figure. Because it's Figure's child elem)
		    __init__
			getPossibleMoves
			getAttackingSquares
			getMoves
			
		params:
			(all parametres of Figure. Because it's Figure's child elem)
			img
			notation'''
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		super().__init__(pos, color, board)

		img_path = 'imgs/' + color[0] + '_pawn.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 35, board.square_height - 35))

		self.notation = 'P'


	def getPossibleMoves(self, board):
		'''get possible moves of figure'''
		possible_moves = []
		moves = []

		if (self.color == 'white'):
			moves.append((0, -1))
			if (not self.has_moved):
				moves.append((0, -2))

		elif (self.color == 'black'):
			moves.append((0, 1))
			if (not self.has_moved):
				moves.append((0, 2))

		for move in moves:
			new_pos = (self.x, self.y + move[1])
			if (new_pos[1] < 8 and new_pos[1] >= 0):
				possible_moves.append(board.getSquareFromPos(new_pos))

		return possible_moves


	def getMoves(self, board):
		moves = []
		for square in self.getPossibleMoves(board):
			if (square.occupying_figure != None):
				break
			else:
				moves.append(square)

		if (self.color == 'white'):
			if (self.x + 1 < 8 and self.y - 1 >= 0):
				square = board.getSquareFromPos((self.x + 1, self.y - 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						moves.append(square)
			if (self.x - 1 >= 0 and self.y - 1 >= 0):
				square = board.getSquareFromPos((self.x - 1, self.y - 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						moves.append(square)

		elif (self.color == 'black'):
			if (self.x + 1 < 8 and self.y + 1 < 8):
				square = board.getSquareFromPos((self.x + 1, self.y + 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						moves.append(square)
			if (self.x - 1 >= 0 and self.y + 1 < 8):
				square = board.getSquareFromPos((self.x - 1, self.y + 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						moves.append(square)

		return moves

	def getAttackingSquares(self, board):
		'''get possible attacks of pawn(this figure moves vertical, but has diagonal attack)'''
		attacking_squares = self.getMoves(board)
		return [i for i in attacking_squares if i.x != self.x]