'''imports required in our file'''
import pygame
from classes.Figure import Figure

class Pawn(Figure):
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		super().__init__(pos, color, board)

		img_path = 'imgs/' + color[0] + '_pawn.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 35, board.square_height - 35))

		self.notation = 'P'


	def getPossibleMoves(self, board):
		'''get possible moves of figure'''
		output = []
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
				output.append(board.getSquareFromPos(new_pos))

		return output


	def getMoves(self, board):
		output = []
		for square in self.getPossibleMoves(board):
			if (square.occupying_figure != None):
				break
			else:
				output.append(square)

		if (self.color == 'white'):
			if (self.x + 1 < 8 and self.y - 1 >= 0):
				square = board.getSquareFromPos((self.x + 1, self.y - 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						output.append(square)
			if (self.x - 1 >= 0 and self.y - 1 >= 0):
				square = board.getSquareFromPos((self.x - 1, self.y - 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						output.append(square)

		elif (self.color == 'black'):
			if (self.x + 1 < 8 and self.y + 1 < 8):
				square = board.getSquareFromPos((self.x + 1, self.y + 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						output.append(square)
			if (self.x - 1 >= 0 and self.y + 1 < 8):
				square = board.getSquareFromPos((self.x - 1, self.y + 1))
				if (square.occupying_figure != None):
					if (square.occupying_figure.color != self.color):
						output.append(square)

		return output

	def attackingSquares(self, board):
		'''get possible attacks of pawn(this figure moves vertical, but has diagonal attack)'''
		moves = self.getMoves(board)
		return [i for i in moves if i.x != self.x]