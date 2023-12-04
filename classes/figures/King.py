'''imports required in our file'''
import pygame
from classes.Figure import Figure

class King(Figure):
	''' class King, which is child class of Figure.
	  	Object contains chess figure King.

	    functions:
			(all functions of Figure. Because it's Figure's child elem)
		    __init__
			getPossibleMoves
			canCastle
			getValidMoves

		params:
			(all parametres of Figure. Because it's Figure's child elem)
			img
			notation'''
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		super().__init__(pos, color, board)

		img_path = 'imgs/' + color[0] + '_king.png'
		self.img = pygame.image.load(img_path)
		self.img = pygame.transform.scale(self.img, (board.square_width - 20, board.square_height - 20))

		self.notation = 'K'


	def getPossibleMoves(self, board):
		'''get possible moves of figure'''
		possible_moves = []
		moves = [
			(0,-1), # north
			(1, -1), # north-east
			(1, 0), # east
			(1, 1), # south-east
			(0, 1), # south
			(-1, 1), # south-west
			(-1, 0), # west
			(-1, -1), # north-west
		]

		for move in moves:
			new_pos = (self.x + move[0], self.y + move[1])
			if (new_pos[0] < 8 and new_pos[0] >= 0 and new_pos[1] < 8 and new_pos[1] >= 0):
				possible_moves.append([board.getSquareFromPos(new_pos)])

		return possible_moves

	def canCastle(self, board):
		'''returns bool(can king and rook do castle)'''
		if not self.has_moved:

			if self.color == 'white':
				queenside_rook = board.getFigureFromPos((0, 7))
				kingside_rook = board.getFigureFromPos((7, 7))
				if queenside_rook != None:
					if not queenside_rook.has_moved:
						if ([board.getFigureFromPos((i, 7)) for i in range(1, 4)] == [None, None, None]):
							return 'queenside'
				if kingside_rook != None:
					if not kingside_rook.has_moved:
						if ([board.getFigureFromPos((i, 7)) for i in range(5, 7)] == [None, None]):
							return 'kingside'
				

			elif (self.color == 'black'):
				queenside_rook = board.getFigureFromPos((0, 0))
				kingside_rook = board.getFigureFromPos((7, 0))
				if (queenside_rook != None):
					if not queenside_rook.has_moved:
						if ([board.getFigureFromPos((i, 0)) for i in range(1, 4)] == [None, None, None]):
							return 'queenside'
				if (kingside_rook != None):
					if (not kingside_rook.has_moved):
						if ([board.getFigureFromPos((i, 0)) for i in range(5, 7)] == [None, None]):
							return 'kingside'


	def getValidMoves(self, board):
		valid_moves = []
		for square in self.getMoves(board):
			if (not board.isCheck(self.color, board_change=[self.pos, square.pos])):
				valid_moves.append(square)

		if (self.canCastle(board) == 'queenside'):
			valid_moves.append(board.getSquareFromPos((self.x - 2, self.y)))
		if (self.canCastle(board) == 'kingside'):
			valid_moves.append(board.getSquareFromPos((self.x + 2, self.y)))

		return valid_moves