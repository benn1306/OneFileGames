import pygame as pg
import random 

screen_width,screen_height = 700,700
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('jump')
clock = pg.time.Clock()


class game_object:
    def __init__(self,collumn):
        self.height,self.width = random.randint(60,80),screen_width//7
        self.collumn = collumn
        self.x,self.y = collumn*100,0
        self.speed = 1
        self.falling = True
        
    def fall(self):   
        global collumns   
        count = -1 
        for i in range(len(collumns[self.collumn])):
            count += 1
            if count == 0 and self.y == collumns[self.collumn][i].y:
                    if self.y <= screen_height - self.height:
                        self.y += self.speed
                        self.falling = True
                    else:
                        self.falling = False
            i -= 1
            if collumns[self.collumn][i] != self and collumns[self.collumn][i+1] == self:
                if self.y <= collumns[self.collumn][i].y - self.height:
                    self.y += self.speed
                    self.falling = True
                else:
                    self.falling = False
        self.rect = pg.Rect(self.x,self.y,self.width,self.height)
        self.danger_rect = pg.Rect(self.x,self.y + self.height - 10, self.width, 10)
    def draw(self):
        pg.draw.rect(screen,('blue'),self.rect)
        pg.draw.rect(screen,'red',self.danger_rect)

class Player:
    def __init__(self):
        self.height,self.width = 50,40
        self.speed = 5
        self.x,self.y = screen_width//2 - self.width , screen_height - self.height
        self.gravity, self.jump_vel, self.jump_height, self.jumping = 1,20,20,False
        self.on_ground, self.falling_plat, self.grav = True, False, 1
    def jump(self,keys):
        if keys[pg.K_SPACE]:
            self.jumping = True
            self.on_ground = False
        if self.jumping:
            self.y -= self.jump_vel
            self.jump_vel -= self.gravity
            if self.jump_vel < -self.jump_height:
                self.jumping = False
                self.on_ground = True
                self.jump_vel = self.jump_height

        if self.falling_plat == True:
            self.y += 1
        if not self.falling_plat:
            if not self.y + self.height >= screen_height and not self.jumping:
                floating = True
                for j in collumns:
                    for item in j:
                        if self.y + self.height == item.y and item.x - self.width <= self.x <= item.x + item.width:
                                floating = False
                                self.y = item.y - self.height
                if floating == False:
                    self.grav = 1
                if floating:
                    self.y += self.grav
                    self.grav += 1



    def move(self,keys):
        if keys[pg.K_a] and self.x > 0:
            self.x -= self.speed
        if keys[pg.K_d] and self.x < screen_width-self.width:
            self.x += self.speed

    def draw_char(self):
        self.col = self.x//100
        self.rect = pg.Rect(self.x,self.y,self.width,self.height)
        pg.draw.rect(screen,'black',self.rect)

def collision_detection(player, game_object):
    player_rect = pg.Rect(player.x, player.y, player.width, player.height)
    game_object_rect =  game_object.rect
    game_object_death = game_object.danger_rect
    if player_rect.colliderect(game_object_death):
        return False
    if player_rect.colliderect(game_object_rect):
        player.on_ground = True
        player.y = game_object.y - player.height
        if game_object.falling:
            player.falling_plat = True
        else:
            player.falling_plat = False

                
#set screen up
def screen_bg():
    screen.fill((84,190,193))
    for i in range(0,screen_width//100):
        if i%2 == 0: 
            pg.draw.rect(screen,(145,216,245),(i*100,0,100,screen_height))
      
def game_loop():
    global collumns
    run = True
    collumns = [[]for i in range(0,screen_width//100)]
    player = Player()
    while run == True:
        if random.randint(1,100) == 1:
            num = random.randint(0,screen_width//100 - 1)
            collumns[num].append(game_object(num))
        screen_bg()
        for col in collumns:
            for c_object in col:
                c_object.fall()
                collision_detection(player,c_object)
                if collision_detection(player,c_object) == False:
                    run = False
                c_object.draw()
        
        player.draw_char()


        keys = pg.key.get_pressed()
        player.jump(keys)
        player.move(keys)

        if player.y <= 0:
            run = False
        pg.display.update()
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
    return

while True:
    game_loop()
