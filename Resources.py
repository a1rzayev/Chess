import os
import pygame
from tkinter.messagebox import askyesno

WINDOW_SIZE = (1200, 800)

def initializeFile():
	'''checks if file is not exist, log.txt will be created to log our games(movements, result of game)'''
	if(os.path.exists("log.txt") == False):
		f = open("log.txt", 'a')
		f.close()

def appendFile(text):
	'''appends information to the end of the file(log.txt)'''
	f = open("log.txt", "a")
	f.write(text)
	f.close()
    
def initializeScreen():
	'''initializes our screen, to display'''
	pygame.display.set_caption("Chess")
	icon = pygame.image.load("imgs/icon.png")
	pygame.display.set_icon(icon)

def draw(screen, board):
	'''draw elements on our screen to let user see elements'''
	screen.fill([255, 255, 255])
	board.draw(screen)
	
	turn_font = pygame.font.SysFont("Arial", 40)
	index_font = pygame.font.SysFont("Arial", 20)
	pygame.draw.rect(screen, (100, 100, 100), (800, 0, 400, 100))
	letter = turn_font.render(f'{board.turn} plays', True, (0,0,0))
	screen.blit(letter, (900, 25))

	for i in range(8):
		letter = index_font.render(f'{chr(65+i)}', True, (0, 0, 0))
		number = index_font.render(f'{str(8-i)}', True, (0, 0, 0))
		screen.blit(letter, (i*100 + 10, 0))
		screen.blit(number, (0, i*100 + 10))

	pygame.display.update()

def gameProcess(board, screen, restart):
	'''gameloop. all operations go here.'''
	is_running = True
	print("\ngame starts!")
	print("white plays")
	appendFile("game starts!\n")
	for row in board.config:
		print(row)
	while is_running:
		draw(screen, board)
		mx, my = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = not askyesno(title='Exit', message='Are you sure you want to quit?')
				if(is_running == False):
					appendFile(board.toReadableConfig())
					appendFile('game was closed\n\n')
					print('game was closed')
					return False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if (event.button == 1 and mx <= 800 and my <= 800):
					board.handleClick(mx, my)

		if board.isCheckmate('black'):
			print('White wins!')
			appendFile(board.toReadableConfig())
			appendFile('White wins!\n\n')
			restart = askyesno(title='White wins!', message='Do you want to play again?')
			is_running = False
		elif board.isCheckmate('white'):
			print('Black wins!')
			appendFile(board.toReadableConfig())
			appendFile('Black wins!\n\n')
			restart = askyesno(title='Black wins!', message='Do you want to play again?')
			is_running = False
	return restart