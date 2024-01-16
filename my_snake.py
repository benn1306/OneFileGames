#importing the usual bits and bobs
import pygame as pg
import random

#using a class to contain it all so i dont need global variables (i prefer oop)
class SnakeGame:
    def __init__(self):
        #initiating pygame
        pg.init()
        #the time
        self.clock = pg.time.Clock()
        #screen is defined 
        self.screen_width, self.screen_height = 600, 600
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Snake")
        #constants (they dont change)
        self.FOOD_SIZE = 10
        self.SNAKE_SIZE = 10
        self.SPEED = 15
        #variables (they change)
        self.food_x, self.food_y = self.screen_width // 2 + self.SNAKE_SIZE * 3, self.screen_height // 2
        self.snake_body = []
        self.snake_length = 1
        self.snake_y, self.snake_x = self.screen_height // 2, self.screen_width // 2
        self.direction = [0, 0]
    #snake logic (was initally just going to be movement but also has growing kinda)
    def snake_movement(self, keys):
        #which way (with vectors)
        if keys[pg.K_UP] and self.direction != [0, self.SNAKE_SIZE]:
            self.direction = [0, -self.SNAKE_SIZE]
        elif keys[pg.K_DOWN] and self.direction != [0, -self.SNAKE_SIZE]:
            self.direction = [0, self.SNAKE_SIZE]
        elif keys[pg.K_LEFT] and self.direction != [self.SNAKE_SIZE, 0]:
            self.direction = [-self.SNAKE_SIZE, 0]
        elif keys[pg.K_RIGHT] and self.direction != [-self.SNAKE_SIZE, 0]:
            self.direction = [self.SNAKE_SIZE, 0]
        #affecting position with the vector
        self.snake_x += self.direction[0]
        self.snake_y += self.direction[1]
        #redefining the snake head at the front most position
        snake_head = [self.snake_x, self.snake_y]
        self.snake_body.append(snake_head)
        #if that new head means the snake is too long cut off the tail
        if len(self.snake_body) > self.snake_length:
            del self.snake_body[0]

        self.draw_snake()
    #food logic
    def food(self):
        self.draw_food(self.food_x, self.food_y)
        food_rect = pg.Rect(self.food_x, self.food_y, self.FOOD_SIZE, self.FOOD_SIZE)
        #did i eat it 
        if food_rect.colliderect(self.snake_x, self.snake_y, self.SNAKE_SIZE, self.SNAKE_SIZE):
            self.snake_length += 1
            self.food_x, self.food_y = random.randrange(0, self.screen_width), random.randrange(0, self.screen_height)
    #showing snake
    def draw_snake(self):
        for segment in self.snake_body:
            pg.draw.rect(self.screen, 'green', (segment[0], segment[1], self.SNAKE_SIZE, self.SNAKE_SIZE), 3)
    #showing any food
    def draw_food(self, food_x, food_y):
        pg.draw.rect(self.screen, 'red', (food_x, food_y, self.FOOD_SIZE, self.FOOD_SIZE))
    #writing the score in top left
    def draw_score(self):
        font = pg.font.Font(None, 30)
        score = font.render("Score: " + str(self.snake_length - 1), True, 'white')
        self.screen.blit(score, (10, 10))
    #all logic for game combined
    def game_loop(self):
        run = True
        #actual game loop 
        while run:
            #background and calling functions
            self.screen.fill('black')
            self.food()
            keys = pg.key.get_pressed()
            self.snake_movement(keys)
            self.draw_score()
            #update screen to show new things and update clock with pace of snake 
            pg.display.update()
            self.clock.tick(self.SPEED)
            #to leave if you want
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            #death by wall
            if self.snake_body[-1][0] <= 0 or self.snake_body[-1][0] >= (self.screen_width - self.SNAKE_SIZE) or self.snake_body[-1][1] <= 0 or self.snake_body[-1][1] >= (self.screen_height - self.SNAKE_SIZE):
                run = False
            #death by running into self
            for segment in self.snake_body[:-1]:
                if segment == self.snake_body[-1]:
                    run = False
        #quit when i want
        pg.quit()

#so if i import this it wont automatically start playing
if __name__ == "__main__":
    game = SnakeGame()
    game.game_loop()
