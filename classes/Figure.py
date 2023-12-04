class Figure:
	
	def __init__(self, pos, color, board):
		'''initializes element of our class. this function also calls constructor'''
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.color = color
		self.has_moved = False
		
	def move(self, board, square, force=False):

		for i in board.squares:
			i.highlight = False

		if (square in self.getValidMoves(board) or force):
			prev_square = board.getSquareFromPos(self.pos)
			self.pos, self.x, self.y = square.pos, square.x, square.y

			prev_square.occupying_figure = None
			square.occupying_figure = self
			board.selected_figure = None
			self.has_moved = True

			# Pawn promotion
			if (self.notation == ' '):
				if (self.y == 0 or self.y== 7):
					from classes.figures.Queen import Queen
					square.occupying_figure = Queen((self.x, self.y), self.color, board)

			# Move rook if king castles
			if (self.notation == 'K'):
				if (prev_square.x - self.x == 2):
					rook = board.getFigureFromPos((0, self.y))
					rook.move(board, board.getSquareFromPos((3, self.y)), force=True)
				elif (prev_square.x - self.x == -2):
					rook = board.getFigureFromPos((7, self.y))
					rook.move(board, board.getSquareFromPos((5, self.y)), force=True)

			return True
		else:
			board.selected_figure = None
			return False


	def getMoves(self, board):
		moves = []
		for direction in self.getPossibleMoves(board):
			for square in direction:
				if (square.occupying_figure is not None):
					if (square.occupying_figure.color == self.color):
						break
					else:
						moves.append(square)
						break
				else:
					moves.append(square)

		return moves


	def getValidMoves(self, board):
		valid_moves = []
		for square in self.getMoves(board):
			if (not board.isCheck(self.color, board_change=[self.pos, square.pos])):
				valid_moves.append(square)

		return valid_moves

	def attackingSquares(self, board):
		return self.getMoves(board)