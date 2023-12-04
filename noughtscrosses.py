#importing pygame
import pygame as pg
pg.init()

#whats the time?
clock = pg.time.Clock()

#defining screen
display_height,display_width = (300,300)
screen = pg.display.set_mode((display_height,display_width))
pg.display.set_caption("Noughts and Crosses")

#setting text variables
font = pg.font.Font(None,80)
font_small = pg.font.Font(None, 15)
draw_txt = font.render('DRAW',True,'white')
o_win_txt = font.render('O WIN',True,'white')
x_win_txt = font.render('X WIN',True,'white')
cont_txt = font_small.render('Space to continue or Esc to leave',True,"gray70")

#writing game logic
def game_loop():
    #setting game variables and lists

    run = True

    turn = 0

    rect_list = []
    played_list = []
    rect_assigned = []
    o_list = []
    x_list = []

    count = 0

    x_win = False
    o_win =False
    draw = False

    screen.fill("white")
    #drawing grid and assigning each slot a box
    for i in range (0,300,100):
            for j in range (0,300,100):
                pg.draw.line(screen,"black",(i,j),(i+300,j))
                pg.draw.line(screen,"black",(i+100,j),(i+100,j+300))
                
                rect_list.append([i,j,100,100])
                rect_assigned.append(count)
                count += 1
    count = 0

    #proper logic init
    while run == True:
        #where mouse
        mouse = pg.mouse.get_pos()

        #let me out pls
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False

            #seeing if click and then finding where
            if event.type == pg.MOUSEBUTTONDOWN :
                if (len(played_list)<9):    
                    for i in rect_list:
                        crect = pg.Rect(i[0],i[1],i[2],i[3])
                        count+= 1
                        if crect.collidepoint(mouse):
                            location = crect
                            box = count
                    count = 0
                    #who clicked, drawing their click and did they win
                if box not in played_list:    
                    if turn % 2 == 0:
                        center = (location[0]+50,location[1]+50)
                        pg.draw.circle(screen,"black",center,50,3)
                        played_list.append(box)
                        o_list.append(box)
                        if (1 in o_list and 2 in o_list and 3 in o_list) or (4 in o_list and 5 in o_list and 6 in o_list) or (7 in o_list and 8 in o_list and 9 in o_list) or (1 in o_list and 5 in o_list and 9 in o_list) or (7 in o_list and 5 in o_list and 3 in o_list) or (1 in o_list and 4 in o_list and 7 in o_list) or (2 in o_list and 5 in o_list and 8 in o_list) or (3 in o_list and 6 in o_list and 9 in o_list):
                            o_win = True
                        else:
                            turn+=1
                    elif turn % 2 == 1:
                        pg.draw.line(screen,"black",(location[0],location[1]),(location[0]+100,location[1]+100),3)
                        pg.draw.line(screen,"black",(location[0]+100,location[1]),(location[0],location[1]+100),3)
                        played_list.append(box)
                        x_list.append(box)
                        if (1 in x_list and 2 in x_list and 3 in x_list) or (4 in x_list and 5 in x_list and 6 in x_list) or (7 in x_list and 8 in x_list and 9 in x_list) or (1 in x_list and 5 in x_list and 9 in x_list) or (7 in x_list and 5 in x_list and 3 in x_list) or (1 in x_list and 4 in x_list and 7 in x_list) or (2 in x_list and 5 in x_list and 8 in x_list) or (3 in x_list and 6 in x_list and 9 in x_list):
                            x_win = True
                        else:
                            turn+=1
                #what happens when they win or draw
                elif x_win == False and o_win == False and (len(played_list)>=9):
                    screen.fill('black')
                    screen.blit(draw_txt,(60,130))
                    screen.blit(cont_txt,(55,200))
                    draw = True
                if x_win == True:
                    screen.fill('black')
                    screen.blit(x_win_txt,(60,130))
                    screen.blit(cont_txt,(55,200))
                if o_win == True:
                    screen.fill('black')
                    screen.blit(o_win_txt,(60,130))
                    screen.blit(cont_txt,(55,200))
        #play again or nah
        if o_win or x_win or draw:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                return True
            elif keys[pg.K_ESCAPE]:
                run = False
        #showing everything and counting ms
        pg.display.update()
        clock.tick(60)
    pg.quit()
    return False

#logic for playing again
while game_loop():
    game_loop()
