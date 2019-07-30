import pygame
import random
import os
import time

WIN_WIDTH = 400
WIN_HEIGHT = 800
PIPE_VEL = 3

#pipe_img = pygame.image.load(os.path.join("",""))
#bg = pygame.image.load(os.path.join("",""))
#bird_image = pygame.image.load(os.path.join("",""))


class Bird:
	"""
	Bird class representing the flappy bird
	"""
	WIN_HEIGHT = 0
	WIN_WIDTH = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.gravity = 9.8
		self.tilt = 0  # degrees to tilt 
		self.tick_count = 0
		self.vel = 0
		self.height = self.y

	def jump(self):
		"""
		make the bird jump
		"""
		self.vel = -10
		self.tick_count = 0
		self.height = self.y

	def move(self):
		"""
		make the bird move
		"""
		self.tick_count += 1

		self.y += self.height + self.vel*(self.tick_count/30) + 0.5*(9.8)*(self.tick_count)**2  # calculate displacement

		if self.vel > 0:  # tilt down
			self.tilt -= 0.5
		else:  # tilt up
			self.tilt += 0.5


	def draw(self, win):
		"""
		draw the bird
		"""
		pass


class Pipe():
	"""
	represnts a pipe object
	"""
	WIN_HEIGHT = 0
	WIN_WIDTH = 0
	WIDTH = 100

	def __init__(self, x, y):
		"""
		initialize pipe object

		:param x: int
		:param y: int
		:return" None
		"""
		self.x = x
		self.y = y
		self.height = 0
		self.gap = 100  # gap between top and bottom pipe

		# where the top and bottom of the pipe is
		self.top = 0
		self.bottom = 0

		self.set_height()

	def set_height(self):
		"""
		set the height of the pipe, from the bottom of the screen
		:return: None
		"""
		offset = 100
		self.height = random.randrange(offset, WIN_HEIGHT-offset)

	def collide(self, pos):
		"""
		returns if a point is colliding with the pipe

		:param pos: 2d tuple (x,y)
		:return: Bool
		"""
		pass

def menu_screen(win):
	"""
	the menu screen that will start the game

	:param win: the pygame window surface
	:return: None
	"""
	pass

def end_screen(win):
	"""
	display an end screen when the player loses
	:param win: the pygame window surface
	:return: None
	"""
	pass

def draw_window(win, bird, pipes, score):
	"""
	draws the windows for the main game loop
	:param win: pygame window surface
	:param bird: a Bird object
	:param pipes: List of pipes
	:param score: score of the game (int)
	"""
	win.blit(bg, (0,0))

	for pipe in pipes:
		pipe.draw(win)

	bird.draw(win)

	pygame.display.update()


def main(win):
	"""
	Runs the main game loop

	:param win: pygame window surface
	:return: None
	"""
	bird = Bird()
	pipes = []

	clock = pygame.time.Clock()
	lost = False

	run = True
	while run:
		clock.tick(30)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.key == pygame.K_SPACE:
					bird.jump()
					print("jump")

		bird.move()

		for pipe in pipes:
			if pipe.collide(bird.x, bird.y):
				print("bird hit pipe")
				lost = True	

		if lost:
			break

	bird.die()
	end_screen()


