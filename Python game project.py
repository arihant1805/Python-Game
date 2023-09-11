import pygame
import time
import random

snake_speed = 20
window_x = 1080
window_y = 720

# defining colors
# i m trying to give it the color of the Python Language
# (Like python color snake and Metallic blue BG)
metallic_blue = pygame.Color(79,115,142)
white = pygame.Color(255, 0, 0)
red = pygame.Color(0, 0, 0)
python_yellow = pygame.Color(255,211,67)
blue = pygame.Color(0, 0, 255)


pygame.init()
pygame.display.set_caption('Python Game by Arihant')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
snake_position = [150, 50]
snake_body = [ [150, 50],
				[140, 50],
				[130, 50],
				[120, 50],
				[110, 50],
	            [100, 50],
				[90, 50],
				[80, 50],
				[70, 50],
				[60, 50],
				[50, 50],
				[40, 50],
				[30, 50],
				[20, 50],
				[10, 50]
			]
fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
change_to = direction
score = 0
def show_score(choice, color, font, size):

	score_font = pygame.font.SysFont(font, size)
	
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	score_rect = score_surface.get_rect()
	game_window.blit(score_surface, score_rect)

def game_over():
	my_font = pygame.font.SysFont('times new roman', 50)
	game_over_surface = my_font.render('GAMEOVER Your Score is : ' + str(score), True, (255,50,0))
	game_over_rect = game_over_surface.get_rect()
	game_over_rect.midtop = (window_x/2, window_y/3)
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit()
	quit()
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores will be
	# incremented by 10
	# also the speed will be increased by 1
	snake_body.insert(0, list(snake_position))
	if (snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1])or(snake_position[0] == fruit_position[0]+10 and snake_position[1] == fruit_position[1]+10):
		score += 10
		snake_speed+=1
		fruit_spawn = False
	else:
		snake_body.pop()
		
	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10,
						random.randrange(1, (window_y//10)) * 10]
		
	fruit_spawn = True
	game_window.fill(metallic_blue)
	# here we are designing the snake such that
	# it will be growing rapidly in front and getting thin at the last gradually
	# to do this i have used different loops
	x=0.0
	y=5
	for pos in snake_body:
		if x==10:
			y=-.2

		pygame.draw.rect(game_window, python_yellow, pygame.Rect(
		pos[0], pos[1], x, x))
		x+=y
	# i took the fruit size as 20*20 
	pygame.draw.rect(game_window, white, pygame.Rect(
	fruit_position[0], fruit_position[1], 20, 20))

	# Game will not be over if snake touches the window wnd it will
	# only end if it touches his own body
	if snake_position[0] < 0 :
		snake_position[0]=window_x-10
	if snake_position[0] > window_x-10:
		snake_position[0]=0
	if snake_position[1] < 0 :
		snake_position[1]=window_y-10
	if snake_position[1] > window_y-10:
		snake_position[1]=0
	# Touching the snake body
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()
	# displaying score continuously
	show_score(1, (255,255,255), 'times new roman', 30)
	
	pygame.display.update()

	fps.tick(snake_speed)
