import pygame
from Resources import *
from classes.Board import Board

if __name__ == "__main__":
	'''main function. main stream to do operations'''
	pygame.init()
	screen = pygame.display.set_mode(WINDOW_SIZE)
	playing = True
	while(playing):
		board = Board(800, 800)
		initializeScreen()
		initializeFile()
		playing = gameProcess(board, screen, playing)