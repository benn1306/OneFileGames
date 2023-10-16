#importing pygame
import pygame
import random
from pygame.locals import *
pygame.init()

#Making custom events for the end
end_event = pygame.USEREVENT + 1
#Adding a timer which triggers the events when a number of ms have passed
pygame.time.set_timer(end_event, 10000)

#Getting the time in ms
clock = pygame.time.Clock()

#Getting a random letter 
def letter():
    letters = [": A",": B",": C",": D",": E",": F",": G",": H",": I",": J",": K",": L",": M",": N",": O",": P",": Q",": R",": S",": T",": U",": V",": W",": X",": Y",": Z"]
    keylet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    rand = random.randint(0,25)
    key = keylet[rand]
    let = letters[rand]
    return let, key
currentlet = letter()

#Defining screen
screen = pygame.display.set_mode([500,500])
screen.fill((150,30,90))
pygame.display.flip()

#Defining variables
run = True
count = 1
play = True

#The first letter
font = pygame.font.SysFont('Arial', 32)
text = font.render((str(count-1)+str(currentlet[0])), True, (40,40,70), (10,80,2))            
textrect = text.get_rect()
textrect.center = (500 // 2, 500 // 2)
#Updating the screen
screen.blit(text, textrect)
pygame.display.flip()

#Starting the game loop
while run == True:
    for event in pygame.event.get(): 
        #Checking for key presses        
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == currentlet[1] and play == True:
                #Random numbers for colour
                num = random.randint(1,255)
                num2 = random.randint(1,255)
                num3 = random.randint(1,255)
                #Random location for text
                snum = random.randint(50,450)
                snum2 = random.randint(50,450)
                #Changing screen colour
                screen.fill((num,num2,num3))
                #calling random letter function
                currentlet = letter()
                text = font.render((str(count)+str(currentlet[0])), True, (num,num2,num3), (num2,num3,num))
                count += 1
                textrect.center = (snum , snum2)  

                if play == False:
                    screen.blit(text2, textrect2)

                #Updating screen
                screen.blit(text, textrect)
                pygame.display.flip()
            elif event.key == K_SPACE:
                play = True
        
        #Showing score
        elif event.type == end_event:
            text_1 = (str(((count-1)/(10/600))+"keys/second"))
            dfont = pygame.font.SysFont('Arial', 20)
            text2 = font.render((text_1), True, (0,0,0), (200,200,200))
            textrect2 = text2.get_rect()
            textrect2.center = (500 // 2, 500 // 2)
            screen.blit(text2, textrect2)
            pygame.display.flip()
            play = False

#Ending the program
        if event.type == pygame.QUIT:
            run = False
