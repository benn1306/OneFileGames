#importing modules
import pygame as pg
import random
#initiate pygame
pg.init()

#define screen
screen_width,screen_height = 500,500
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("pong breaker")
#define time
clock = pg.time.Clock()

#defining variables and lists
score_0 = 0
score_1 = 0
brick_list = []
brick_list2 = []

#paddle
class paddle:
    def __init__(self,y,speed):
        #defining things every paddle needs
        self.length,self.height = screen_width//10, screen_height//50
        self.x,self.y = screen_width//2 - self.length//2, y
        self.rect = pg.Rect(self.x,self.y,self.length,self.height)
        self.colour = 'white'
        self.SPEED = speed
    #the paddle can draw itself
    def draw(self):
        pg.draw.rect(screen,self.colour,self.rect)
    #the paddle moves
    def move(self,direction):
        self.rect.x += direction * self.SPEED
        
#ball 
class Ball:
    def __init__(self):
        #every ball has to have these
        self.radius = 5
        self.x,self.y = screen_width//2 - self.radius,screen_height//2
        self.direction = [0,1]
        self.SPEED = 5
    #draw balls
    def draw(self):
        pg.draw.circle(screen,"white",(self.x,self.y),self.radius)
    #moving with conditions
    def move(self,player_paddle,enemy_paddle):
        global score_1,score_0
        #what the ball is 
        self.rect = pg.Rect(self.x,self.y,self.radius*2,self.radius*2)
        #if it hits floor or ceiling flip y vector but keep x
        if self.y >= screen_height or self.y <= 0:
            self.direction = [self.direction[0],-self.direction[1]]
        #if it hits walls flip x vector but keep y
        if self.x <= 0 or self.x >= screen_width:
            self.direction = [-self.direction[0],self.direction[1]]

        #if it hits a paddle flip y keep x (if it had no x give it a random one)
        if player_paddle.rect.colliderect(self.rect) or enemy_paddle.rect.colliderect(self.rect):
            if self.direction[0] == 0:
                self.direction = [random.randint(-1,1),-self.direction[1]]
            else:
                self.direction = [self.direction[0],-self.direction[1]]
        
        #if it hits a brick it breaks it and changes direction (or it should at least)
        for i in brick_list:
            if self.rect.colliderect(i.x,i.y,i.size[0],i.size[1]):
                self.direction = [self.direction[0],-self.direction[1]]
                i.breaking(1)
        for j in brick_list2:
            if self.rect.colliderect(j.x,j.y,j.size[0],j.size[1]):
                self.direction = [self.direction[0],-self.direction[1]]
                j.breaking(2)
                
                
        #effecting the ball by its vectors
        self.y += self.direction[1] * self.SPEED
        self.x += self.direction[0] * self.SPEED//2

#writing the scores
def text():
    global score_1,score_0
    font = pg.font.Font(None,30)
    play_score = font.render('Player 1 score: '+ str(score_0), True,'grey30')
    enem_score = font.render('Player 2 score:'+ str(score_1),True,'grey30')
    screen.blit(play_score,(0,screen_height//5 + 20))
    screen.blit(enem_score,(0,screen_height - (screen_height//5 + 20)))

#bricks to break
class brick:
    def __init__(self,x,y):
        self.colour = [random.randrange(0,255),random.randrange(0,256),random.randrange(0,256)]
        self.size = [screen_width//25,screen_height//40]
        self.x = x
        self.y = y
        brick_list.append(self)
    def breaking(self,listnum):
        if listnum == 2:
            brick_list2.remove(self)
        if listnum == 1:
            brick_list.remove(self)

    def draw(self):
        pg.draw.rect(screen,self.colour,(self.x,self.y,self.size[0],self.size[1]))

def player_movement(keys,paddle):
    direction = 0
    if keys[pg.K_LEFT] and paddle.x >= 0:
        direction = -1
    elif keys[pg.K_RIGHT] and paddle.x <= screen_width-paddle.length:
        direction = 1
    return direction

def player_2_movement(keys,paddle):
    direction = 0
    if keys[pg.K_a] and paddle.x >= 0:
        direction = -1
    elif keys[pg.K_d] and paddle.x <= screen_width-paddle.length:
        direction = 1
    return direction

def enemy_movement(ball_pos,paddle):
    direction = 0
    if (ball_pos - paddle) > 0:
        direction = 1
    if (ball_pos - paddle) < 0:
        direction = -1
    return direction

def game_loop():
    run = True
    player_paddle = paddle(screen_height - (screen_height//5 + 19),5)
    enemy_paddle = paddle(screen_height//5 + 10,5)
    ball = Ball()
    for i in range(0,screen_width,screen_width//25):
        for j in range(0, screen_height//5,screen_height//45):
            brick_list.append(brick(i,j))
            brick_list2.append(brick(i,(screen_height)-j-screen_height//45))
    while run:
        screen.fill('black')
        keys = pg.key.get_pressed()
        player_direction = player_movement(keys,player_paddle)
        #enemy_direction = enemy_movement(ball.x,enemy_paddle.rect.centerx)
        enemy_direction = player_2_movement(keys,enemy_paddle)
        player_paddle.move(player_direction)
        enemy_paddle.move(enemy_direction)
        ball.move(player_paddle,enemy_paddle)

        text()
        player_paddle.draw()
        enemy_paddle.draw()
        ball.draw()
        
        for i in brick_list:
            i.draw()
        for j in brick_list2:
            j.draw()
        pg.display.update()
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
    
    pg.quit()

#running loop
game_loop()