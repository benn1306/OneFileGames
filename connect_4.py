#import pygame
import pygame as pg
pg.init()

#set time
clock = pg.time.Clock()

#define screen size
screen_width = 700
screen_height = 600

#make screen
screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('Connect 4')

#function to get grid
def grid():
    for i in range(0,screen_width,100):
        for j in range(0,screen_height,100):
            pg.draw.line(screen,'black',(0,j),(screen_width,j))
            pg.draw.line(screen,'black',(i,0),(i,screen_height))

#circles in the grid obv
def circle(rects):
    for i in rects:
        for j in i:
            pg.draw.circle(screen,'black',(j[0]+50,j[1]+50),40,2)

#making turns
def turns(turn,list_rects,collumn,played_collumns):
    global red_pos,blue_pos
    next_box = len(played_collumns[collumn])
    c_rect = list_rects[collumn][next_box]
    if turn % 2 == 0:
        pg.draw.circle(screen,'red',(c_rect[0]+50,c_rect[1]+50),40)
        red_pos[collumn].append(next_box)

    else:
        pg.draw.circle(screen,'blue',(c_rect[0]+50,c_rect[1]+50),40)
        blue_pos[collumn].append(next_box)

def drawn():
    font_draw = pg.font.SysFont(None, 100)
    draw_txt = font_draw.render('Draw',True,'white')
    f_width,f_height = font_draw.size('Draw')
    screen.fill('black')
    screen.blit(draw_txt,(screen_width//2 - f_width//2,screen_height//2),)

#win cons
def win(r_pos,b_pos):

    #horiontal check
    for i in range(screen_width//100 - 3):
        for j in r_pos[i]:
            if j in r_pos[i] and j in r_pos[i+1] and j in r_pos[i+2] and j in r_pos[i+3]:
                return True,False
    for i in range(screen_width//100 - 3):
        for j in b_pos[i]:
            if j in b_pos[i] and j in b_pos[i+1] and j in b_pos[i+2] and j in b_pos[i+3]:
                return False,True
            
    #vertical check
    for i in range(screen_width//100):
        for j in range(screen_height//100-2):
            if j in r_pos[i] and j+1 in r_pos[i] and j+2 in r_pos[i] and j+3 in r_pos[i]:
                return True,False
    for i in range(screen_width//100):
        for j in range(screen_height//100-2):
            if j in b_pos[i] and j+1 in b_pos[i] and j+2 in b_pos[i] and j+3 in b_pos[i]:
                return False,True
    
    #diagonal check (yikesssss this will be messy)
    for i in range(screen_width//100-3):
        for j in range(screen_width//100-2):
            if j in r_pos[i] and j+1 in r_pos[i+1] and j+2 in r_pos[i+2] and j+3 in r_pos[i+3]:
                return True,False
    for i in range(screen_width//100-3):
        for j in range(screen_width//100-2):
            if j in b_pos[i] and j+1 in b_pos[i+1] and j+2 in b_pos[i+2] and j+3 in b_pos[i+3]:
                return False,True
    #backwards diagonal cos you need a different check (aaaaa that took like 5 mins longer than it should have to figure out)
    for i in range(screen_width//100-3):
        for j in range(screen_width//100,2,-1):
            if j in r_pos[i] and j-1 in r_pos[i+1] and j-2 in r_pos[i+2] and j-3 in r_pos[i+3]:
                return True,False
    for i in range(screen_width//100-3):
        for j in range(screen_width//100,2,-1):
            if j in b_pos[i] and j-1 in b_pos[i+1] and j-2 in b_pos[i+2] and j-3 in b_pos[i+3]:
                return False,True
    

    return False,False

#ending game if winner/displaying winner ig
def win_txt(rwin,bwin):
    screen.fill('black')
    font = pg.font.SysFont(None,70)
    if rwin or bwin:
        if rwin:
            txt = font.render('Red Wins',True,'white')
            size,s = font.size('Red Wins')
        elif bwin:
            txt = font.render('Blue Wins',True,'white')
            size,s = font.size('Blue Wins')
        screen.blit(txt,(screen_width//2 - size//2 , screen_height//2))

    
#combining all the game logic so it runs hopefully
def game_loop():
    run = True

    #giving each box in the grid its own values so it can be made into a rect and used easier later + making entire collumns cos I need them for stuff 
    rects = [[[i,j,100,100] for j in range(screen_height,-100,-100)] for i in range(0,screen_width,100)]
    collumns = [[u,0,100,screen_height] for u in range(0,screen_width,100)]
    collumns_play = [[] for i in range(0,screen_width,100)]

    #where has each side put there stuff
    global red_pos,blue_pos
    red_pos = [[] for i in range(0,screen_width,100)]
    blue_pos = [[] for i in range(0,screen_width,100)]

    #end variables
    draw_q = 1
    end = False

    #drawing grid with function i made
    screen.fill('white')
    grid()
    circle(rects)

    turn = 0
    
    while run == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if end == False:
                #finding whhich collumn they put the counter in after a click
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()

                    for u in range(len(collumns)):
                        c_rect = pg.rect.Rect(collumns[u])

                        if c_rect.collidepoint(mouse):
                            #is collumn full???
                            if len(collumns_play[u]) < screen_height//100:
                                current_collumn = u
                                collumns_play[current_collumn].append(len(collumns_play[current_collumn]))
                                #getting turn to happen
                                turns(turn,rects,current_collumn,collumns_play)
                                turn += 1
                            for i in collumns_play:
                                if len(i) >= screen_height//100:
                                    draw_q += 1
                            rwin,bwin = win(red_pos,blue_pos)
                            if rwin or bwin:
                                win_txt(rwin,bwin)
                                end = True
                            if draw_q == screen_width//100:
                                drawn()
                                end = True
                            else:
                                draw_q = 0

        
        
        if end == True:
            font = pg.font.SysFont(None,30)
            width_f,height_f = font.size("Press space to play again or escape to quit.")
            
            txt = font.render("Press space to play again or escape to quit.",True,'gray70')
            screen.blit(txt,(screen_width//2 - width_f//2,screen_height-screen_width//8))
            
            #play again?
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                return
            if keys[pg.K_ESCAPE]:
                run = False
        
        

        pg.display.update()
        clock.tick(60)
    pg.quit()
while True:
    game_loop()