
import pygame
import random

pygame.init()

gameWindow = pygame.display.set_mode((1200, 500))



font=pygame.font.Font('freesansbold.ttf', 32)


def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def screen_text(text,color,x,y):
    text=font.render(text,True,color)
    gameWindow.blit(text,[x,y])



clock = pygame.time.Clock()


def gameloop():
    white=(255,255,255)
    black=(0,0,0)
    blue=(0,0,255)
    red=(255,0,0)
    snake_x = 45
    snake_y = 45
    food_x=random.randint(0,1100)
    food_y=random.randint(0,450)
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    fps = 30
    score=0
    snk_list=[]
    snk_length=1
    exit_game = True
    game_over=True

    while exit_game:

        if not game_over:
            gameWindow.fill((44,83,212))
            screen_text("Game Overrrrr :-( Press Enter to play again!!!",(11, 15, 64),230,230)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            gameWindow.fill((11, 15, 64))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                        
                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x-food_x) < 10 and abs(snake_y-food_y)<10:
                score = score + 1
                screen_text("Score: "+str(score),blue,5,5)
                food_x=random.randint(0,1100)
                food_y=random.randint(0,450)
                snk_length +=5

            screen_text("Score: "+str(score),blue,5,5)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if len(snk_list)>snk_length:
                del snk_list[0]
                
            if snake_x<0 or snake_x>1200 or snake_y<0 or snake_y>500:
                game_over=False

            if head in snk_list[:-1]:
                game_over=False
            
            plot_snake(gameWindow,white,snk_list,snake_size)    

            pygame.draw.rect(gameWindow,red, [food_x, food_y, snake_size, snake_size])
                            

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()