import pygame
import random

# Initialize pygame
pygame.init()

# Set up display dimensions
display_width = 800
display_height = 600

# Load background image
back_image_snow = pygame.image.load('PenguinGame/background.png')
back_image_sand = pygame.image.load('PenguinGame/backgroundtwo.png')
back_image_hallo = pygame.image.load('PenguinGame/backgroundthree.png')
back_image_fazz = pygame.image.load('PenguinGame/backgroundfour.png')
back_image_red = pygame.image.load('PenguinGame/redcarpet.png')
back_image_fam = pygame.image.load('PenguinGame/familyguy.png')
back_image_sch = pygame.image.load('PenguinGame/school.png')

back_image_snow = pygame.transform.scale(back_image_snow, (display_width, display_height))
back_image_sand = pygame.transform.scale(back_image_sand, (display_width, display_height))
back_image_hallo = pygame.transform.scale(back_image_hallo, (display_width, display_height))
back_image_fazz = pygame.transform.scale(back_image_fazz, (display_width, display_height))
back_image_red = pygame.transform.scale(back_image_red, (display_width, display_height))
back_image_fam = pygame.transform.scale(back_image_fam, (display_width, display_height))
back_image_sch = pygame.transform.scale(back_image_sch, (display_width, display_height))

skin = [back_image_snow,back_image_sand,back_image_hallo, back_image_fazz,back_image_red,back_image_fam,back_image_sch]
skinnum = random.randint(0,len(skin))
currentskin = skin[skinnum-1]
# Set up the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pixel Penguin')

# Set up clock
clock = pygame.time.Clock()

# Set up the player
player_width = 50
player_height = 50
player_x = display_width * 0.45
player_y = (display_height * 0.8) +30

# Set up the initial enemy
enemy_width = 30
enemy_height = 60
enemy_speed = 7

# Load images
player_image = pygame.image.load('PenguinGame/player.png')
player_image_pumpkin = pygame.image.load('PenguinGame/playertwo.png')
player_image_purple = pygame.image.load('PenguinGame/playerthree.png')
player_image_ben = pygame.image.load('PenguinGame/playerfour.png')
player_image_among = pygame.image.load('PenguinGame/playerfive.png')
player_image_stew = pygame.image.load('PenguinGame/stewie.png')
player_image_solja = pygame.image.load('PenguinGame/solja.jpeg')

player_image = pygame.transform.scale(player_image, (player_width, player_height))
player_image_pumpkin = pygame.transform.scale(player_image_pumpkin, (player_width, player_height))
player_image_purple = pygame.transform.scale(player_image_purple, (player_width, player_height))
player_image_ben = pygame.transform.scale(player_image_ben, (player_width, player_height))
player_image_among = pygame.transform.scale(player_image_among, (player_width, player_height))
player_image_stew = pygame.transform.scale(player_image_stew, (player_width, player_height))
player_image_solja = pygame.transform.scale(player_image_solja, (player_width, player_height))


player_skin_list = [player_image, player_image_pumpkin, player_image_ben, player_image_purple, player_image_among,player_image_stew,player_image_solja]
player_skin = random.randint(0,len(player_skin_list))
currentplay = player_skin_list[player_skin-1]

enemy_image = pygame.image.load('PenguinGame/enemy.png')
enemy_arrow = pygame.image.load('PenguinGame/arrowprojectile.png')
enemy_lamp = pygame.image.load('PenguinGame/LampPost.png')
enemy_child = pygame.image.load('PenguinGame/enemytwo.png')
enemy_toilet = pygame.image.load('PenguinGame/toilet.png')
enemy_eminem = pygame.image.load('PenguinGame/eminem.jpeg')


enemy_image = pygame.transform.scale(enemy_image, (enemy_width, enemy_height))
enemy_arrow = pygame.transform.scale(enemy_arrow, (enemy_width,enemy_height))
enemy_lamp = pygame.transform.scale(enemy_lamp, (enemy_width,enemy_height))
enemy_child = pygame.transform.scale(enemy_child, (enemy_width,enemy_height))
enemy_toilet = pygame.transform.scale(enemy_toilet, (enemy_width,enemy_height))
enemy_eminem = pygame.transform.scale(enemy_eminem, (enemy_width,enemy_height))


enemy_skin_list = [enemy_image,enemy_arrow,enemy_lamp,enemy_child,enemy_toilet,enemy_eminem]
enemy_skin = random.randint(0,len(skin))
currentenemy = enemy_skin_list[enemy_skin-1]
# Define functions
def player(x, y):
    global currentplay
    game_display.blit(currentplay, (x, y))

def enemy(x, y, w, h):
    global currentenemy
    game_display.blit(currentenemy, (x, y))

def is_overlapping(new_enemy, existing_enemies):
    for enemy in existing_enemies:
        if (new_enemy[0] < enemy[0] + enemy[2] and
            new_enemy[0] + new_enemy[2] > enemy[0]):
            return True
    return False

def game_over():
    global enemy_list,score, currentskin, currentplay, skinnum
    enemy_list = []
    font = pygame.font.Font(None, 40)
    nfont = pygame.font.Font(None, 25)
    currentskin = skin[skinnum-1]
    game_display.blit(currentskin, (0, 0))
    game_over_text = font.render("You Died... Press Space to play again or Escape to exit.", True, "white")
    text_width, text_height = font.size("You Died... Press Space to play again or Escape to exit.")
    score_text = nfont.render(f"Score: {score}", True, "white")
    score_width,score_height = nfont.size(f"Score: {score}")
    game_display.blit(score_text, ((display_width/2)-score_width, display_height/2 + 40))
    game_display.blit(game_over_text, (((display_width / 2)- text_width /2), (display_height / 2)))
    score = 0
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "restart"
                elif event.key == pygame.K_ESCAPE:
                    return "exit"
            elif event.type == pygame.QUIT:
                    return "exit"
            
def game_win():
    global enemy_list,score, currentskin, currentplay
    enemy_list = []
    font = pygame.font.Font(None, 40)
    nfont = pygame.font.Font(None, 25)
    game_display.blit(currentskin, (0, 0))
    game_over_text = font.render("You Won... Press Space to play again or Escape to exit.", True, "white")
    text_width, text_height = font.size("You Won... Press Space to play again or Escape to exit.")
    score_text = nfont.render(f"Score: {score}", True, "white")
    score_width,score_height = nfont.size(f"Score: {score}")
    game_display.blit(score_text, ((display_width/2)-score_width, display_height/2 + 40))
    game_display.blit(game_over_text, (((display_width / 2)- text_width /2), (display_height / 2)))
    score = 0
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "restart"
                elif event.key == pygame.K_ESCAPE:
                    return "exit"
            elif event.type == pygame.QUIT:
                    return "exit"
            
def game_loop(player_x,player_y):
    global player_width, player_height,score, skinnum, currentplay, currentenemy
    game_exit = False
    enemy_count = 1
    enemy_spawn_timer = 0
    score = 0
    new_wave = False
    enemy_list = []
    max = 5
    acceleration = 0.5
    max_speed = 7
    player_speed_x = 0
    count = 0
    enemy_size_reduction_rate = 0.5
    enemy_spawn_timer_iteration = 240

    skinnum = random.randint(0,len(skin))

    player_skin = random.randint(0,len(player_skin_list))
    currentplay = player_skin_list[player_skin-1]    

    enemy_skin = random.randint(0,len(enemy_skin_list))
    currentenemy = enemy_skin_list[enemy_skin-1]

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        # Capture key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            if player_speed_x > -max_speed:
                player_speed_x -= acceleration
        elif keys[pygame.K_RIGHT] and player_x < (display_width - player_width):
            if player_speed_x < max_speed:
                player_speed_x += acceleration
        else:
            if player_speed_x > 0 and player_x < (display_width - player_width):
                player_speed_x -= acceleration/2
            elif player_speed_x < 0 and player_x > 0 :
                player_speed_x += acceleration/2
            else:
                player_speed_x = 0
        player_x += player_speed_x

        currentskin = skin[skinnum-1]
        game_display.blit(currentskin, (0, 0))

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, "white")
        game_display.blit(score_text, (10, 10))

        if new_wave == True:
            text_time += 5
            game_display.blit(new_wave_text, ((display_width / 2),10))
            for enemy_pos in enemy_list:
                if enemy_pos[1] > 540:
                    if enemy_pos in enemy_list:
                        enemy_list.remove(enemy_pos)
            if text_time >= 360:
                new_wave = False
                enemy_list = []
                skinnum = random.randint(0,len(skin))
                
        # Update and draw enemies
        for enemy_pos in enemy_list:
            enemy(enemy_pos[0], enemy_pos[1], enemy_pos[2], enemy_pos[3])
            enemy_pos[1] += enemy_speed

            # Check for collision
            if player_y < enemy_pos[1] + enemy_pos[3] and player_y + player_height > enemy_pos[1]:
                if player_x < enemy_pos[0] + enemy_pos[2] and player_x + player_width > enemy_pos[0]:
                    result = game_over()
                    if result == "exit":
                        game_exit = True
                    if result == "restart":
                        return

            # Reset enemies if they go off the screen
            if enemy_pos[1] > 532:
                enemy_pos[1] = 0 - enemy_pos[3]
                enemy_pos[0] = random.randrange(0, int(display_width - enemy_pos[2]))

        # Add new enemies over time
        enemy_spawn_timer += 1
        
        if enemy_count <= max:
            total_enemies = enemy_count
        else:
            enemy_count = 1
            total_enemies = enemy_count
            enemy_spawn_timer_iteration -= 10
            count += 1
            if count % 2 == 1:
                max += 1
            
            if enemy_spawn_timer_iteration <= 60:
                enemy_list = []
                wresult = game_win()
                if wresult == "exit":
                    game_exit = True
                elif wresult == "restart":
                    return
            else:
                new_wave_text = font.render("New Wave Approaching...",True,"white")
                new_wave = True
                text_time = 0
                wave_text_width,wave_text_height = font.size("New Wave Approaching...")
                game_display.blit(new_wave_text, ((display_width / 2)- wave_text_width,10))
        if enemy_spawn_timer == enemy_spawn_timer_iteration:  # Adjust the rate of enemy spawn here
            for _ in range(total_enemies):
                new_enemy_width = (enemy_width - enemy_size_reduction_rate * enemy_count)
                new_enemy_height = (enemy_height - enemy_size_reduction_rate * enemy_count)
                new_enemy = ([random.randrange(0, int(display_width - new_enemy_width)), (-new_enemy_height), new_enemy_width, new_enemy_height])
                
                while is_overlapping(new_enemy, enemy_list):
                        new_enemy = [random.randrange(0, int(display_width - new_enemy_width)), (-new_enemy_height), new_enemy_width, new_enemy_height]
                enemy_list.append(new_enemy)

            enemy_count+=1
            enemy_spawn_timer = 0
        score += int(len(enemy_list))
            
        player(player_x, player_y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

# Start the game
while True:
    game_loop(player_x,player_y)