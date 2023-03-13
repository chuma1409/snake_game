import random
import pygame;
import time
pygame.init()

black=(0,0,0)
blue = (50, 153, 213)
red=(255,0,0)
white = (255,255,255)
green = (0, 255, 0)


screen_width = 800
screen_height = 600

screen_display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Block eater Snake Game by CHUMA")

game_over = False
snake_body = 10                      

timer = pygame.time.Clock()
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift",30)
score_font = pygame.font.SysFont("comicsansms",30)


def score(points):
    val = font_style.render("Your Score: " +str(points),True,blue)
    screen_display.blit(val,[screen_width/14,screen_height/12])


def snake(snake_list):
    for x in snake_list:
        x1 = x[0]
        x2 = x[1]
        pygame.draw.rect(screen_display,white,[x1,x2,snake_body,snake_body])

def message(msg,color):
    m = font_style.render(msg,True,color)
    screen_display.blit(m,[screen_width/6,screen_height/3])

def snakeLoop():
    game_over = False
    exit_game = False
    
    x_axisChange = 0
    y_axisChange = 0

    x_axis = screen_width/2
    y_axis = screen_height/2

    snake_list = []
    snake_size = 1

    x_food = round(random.randrange(0,screen_width-snake_body)/10.0)*10.0
    y_food = round(random.randrange(0,screen_height-snake_body)/10.0)*10.0

    while not game_over:

        while exit_game == True:
            screen_display.fill(black)
            
            message("Game Over! Press Q to QUIT  or C to PLAY Again",red)
            score(snake_size-1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        exit_game = False
                    if event.key == pygame.K_c:
                        snakeLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                    x_axisChange = -snake_body
                    y_axisChange = 0
                elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                    x_axisChange = snake_body
                    y_axisChange = 0
                elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                    x_axisChange = 0
                    y_axisChange = -snake_body
                elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                    x_axisChange = 0
                    y_axisChange = snake_body

        if x_axis >= screen_width or x_axis < 0 or y_axis >= screen_height or y_axis < 0:
            exit_game = True

        x_axis += x_axisChange
        y_axis += y_axisChange

        screen_display.fill(black)

        pygame.draw.rect(screen_display,green,[x_food,y_food,snake_body,snake_body])
        snake_head = []
        snake_head.append(x_axis)
        snake_head.append(y_axis)
        snake_list.append(snake_head)

        if len(snake_list) > snake_size:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                exit_game = True
        snake(snake_list)
        score(snake_size-1)
        
        pygame.display.update()

        if x_axis == x_food and y_axis == y_food:
            x_food = round(random.randrange(0,screen_width-snake_body)/10.0)*10.0
            y_food = round(random.randrange(0,screen_height-snake_body)/10.0)*10.0
            snake_size+=1

        timer.tick(snake_speed)
# message("Game Over!",red)
# pygame.display.update()
# time.sleep(2)

    pygame.quit()
    quit()

snakeLoop()
