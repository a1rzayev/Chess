import time
from Resources import appendFile
from classes.Square import Square
from classes.figures.Rook import Rook
from classes.figures.Bishop import Bishop
from classes.figures.Knight import Knight
from classes.figures.Queen import Queen
from classes.figures.King import King
from classes.figures.Pawn import Pawn

class Board:
	def __init__(self, width, height):
		'''initializes element of our class. this function also calls constructor'''
		self.letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
		self.width = width
		self.height = height
		self.square_width = 100
		self.square_height = 100
		self.selected_figure = None
		self.turn = 'white'
		self.selected_x = None
		self.selected_y = None
		self.moving_x = 0
		self.moving_y = 0

		self.config = [
			['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
			['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
			['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
			['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
			['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
			['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
			['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
			['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
		]

		self.squares = self.generateSquares()

		self.setup()

	def generateSquares(self):
		'''generate square while initialization of file'''
		squares = []
		for y in range(8):
			for x in range(8):
				squares.append(Square(x, y, self.square_width, self.square_height))

		return squares

	def setup(self):
		'''generate figures while initialization'''
		for y, row in enumerate(self.config):
			for x, piece in enumerate(row):
				if (piece != ''):
					square = self.getSquareFromPos((x, y))

					if (piece[1] == 'R'):
						square.occupying_figure = Rook((x, y), 'white' if piece[0] == 'w' else 'black', self)

					elif (piece[1] == 'N'):
						square.occupying_figure = Knight((x, y), 'white' if piece[0] == 'w' else 'black', self)

					elif (piece[1] == 'B'):
						square.occupying_figure = Bishop((x, y), 'white' if piece[0] == 'w' else 'black', self)

					elif (piece[1] == 'Q'):
						square.occupying_figure = Queen((x, y), 'white' if piece[0] == 'w' else 'black', self)

					elif (piece[1] == 'K'):
						square.occupying_figure = King((x, y), 'white' if piece[0] == 'w' else 'black', self)

					elif (piece[1] == 'P'):
						square.occupying_figure = Pawn((x, y), 'white' if piece[0] == 'w' else 'black', self)
	
	def toReadableConfig(self):
		'''convert config to string'''
		strConfig = ""
		for row in self.config:
			strConfig += f"{row}\n"
		return strConfig

	def handleClick(self, mx, my):
		'''event to click. on click we choose what to do'''
		x = mx // self.square_width
		y = my // self.square_height
		clicked_square = self.getSquareFromPos((x, y))

		if (self.selected_figure is None):
			if (clicked_square.occupying_figure is not None):
				if (clicked_square.occupying_figure.color == self.turn):
					self.selected_figure = clicked_square.occupying_figure
					self.selected_x = x
					self.selected_y = y

		elif (self.selected_figure.move(self, clicked_square)):
			self.turn = 'white' if self.turn == 'black' else 'black'

			self.config[y][x] = self.config[self.selected_y][self.selected_x]
			self.config[self.selected_y][self.selected_x] = '  '

			print(f"{self.letters_list[self.selected_x]}{8 - self.selected_y} --> {self.letters_list[x]}{8 - y}")
			appendFile(f"{self.letters_list[self.selected_x]}{8 - self.selected_y} --> {self.letters_list[x]}{8 - y}\n")

			print(f"\n{self.turn} plays")
			print(self.toReadableConfig())
			
            

		elif (clicked_square.occupying_figure is not None):
			if (clicked_square.occupying_figure.color == self.turn):
				self.selected_figure = clicked_square.occupying_figure

	def isCheck(self, color, board_change=None):
		'''returns if there is check'''
		is_check = False
		king_pos = None

		changing_figure = None
		old_square = None
		new_square = None
		new_square_old_piece = None

		if (board_change is not None):
			for square in self.squares:
				if (square.pos == board_change[0]):
					changing_figure = square.occupying_figure
					old_square = square
					old_square.occupying_figure = None
			for square in self.squares:
				if (square.pos == board_change[1]):
					new_square = square
					new_square_old_piece = new_square.occupying_figure
					new_square.occupying_figure = changing_figure

		pieces = [i.occupying_figure for i in self.squares if i.occupying_figure is not None]

		if (changing_figure is not None):
			if (changing_figure.notation == 'K'):
				king_pos = new_square.pos
		if (king_pos == None):
			for piece in pieces:
				if (piece.notation == 'K'):
					if (piece.color == color):
						king_pos = piece.pos
		for piece in pieces:
			if (piece.color != color):
				for square in piece.attackingSquares(self):
					if (square.pos == king_pos):
						is_check = True

		if (board_change is not None):
			old_square.occupying_figure = changing_figure
			new_square.occupying_figure = new_square_old_piece
		
		# if(is_check):
		# 	self.squares[king_pos[0]][king_pos[1]].color = (128, 0, 0)
		# else:
		# 	self.squares[king_pos[0]][king_pos[1]].color = (0, 0, 0)
		return is_check


	def isCheckmate(self, color):
		'''returns if there is checkmate'''
		is_checkmate = False

		for figure in [i.occupying_figure for i in self.squares]:
			if (figure != None):
				if (figure.notation == 'K' and figure.color == color):
					king = figure

		if (king.getValidMoves(self) == []):
			if (figure.notation != 'K' and figure.color == color):
				king = figure
			elif (self.isCheck(color)):
				is_checkmate = True

		return is_checkmate

	def isDraw(self):
		'''returns if there is draw'''
		is_draw = False
		figures_count = 0
		for figure in [i.occupying_figure for i in self.squares]:
			if (figure == None):
				figures_count += 1
		if (figures_count == 2):
			is_draw = True
		return is_draw


	def getSquareFromPos(self, pos):
		'''returns square by its coordinates on board'''
		for square in self.squares:
			if (square.x, square.y) == (pos[0], pos[1]):
				return square


	def getFigureFromPos(self, pos):
		'''returns figure by its coordinates on board'''
		return self.getSquareFromPos(pos).occupying_figure


	def draw(self, display):
		'''we use recursion here. draw elements(figures and squares) on board'''
		if (self.selected_figure is not None):
			self.getSquareFromPos(self.selected_figure.pos).highlight = True
			for square in self.selected_figure.getValidMoves(self):
				square.highlight = True

		for square in self.squares:
			square.draw(display)

	def timer(self, minutes):
		'''timer that computes time in game'''# isn't ready yet
		seconds = minutes * 60
		start_time = time.time()

		while True:
			elapsed_time = time.time() - start_time
			remaining_time = max(0, seconds - elapsed_time)
			minutes_remaining, seconds_remaining = divmod(remaining_time, 60)
			print(f"Time remaining: {int(minutes_remaining)} minutes {int(seconds_remaining)} seconds", end='\r')
			if (elapsed_time >= seconds):
				break
			time.sleep(1)

		print("\nTimer completed!")