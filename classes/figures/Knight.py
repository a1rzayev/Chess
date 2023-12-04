'''imports required in our file'''
import pygame
from classes.Figure import Figure

class Knight(Figure):
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		super().__init__(pos, color, board)

		img_path = 'imgs/' + color[0] + '_knight.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 20, board.square_height - 20))

		self.notation = 'N'


	def getPossibleMoves(self, board):
		'''get possible moves of figure'''
		possible_moves = []
		moves = [
			(1, -2), # forward2-right1
			(2, -1), # forward1-right2
			(2, 1), # backward1-right2
			(1, 2), # backward2-right1
			(-1, 2), # backward2-left1
			(-2, 1), # backward1-left2
			(-2, -1), # forward1-left2
			(-1, -2) # forward2-left1
		]

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if (new_pos[0] < 8 and new_pos[0] >= 0 and new_pos[1] < 8 and new_pos[1] >= 0):
				possible_moves.append([board.getSquareFromPos(new_pos)])

		return possible_moves