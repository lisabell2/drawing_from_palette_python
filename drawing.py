import pygame
from pygame.locals import * 
pygame.init()


bar_size = (40, 40)
img = pygame.image.load("lorikeet.bmp") #load an image as a Surface

screen = pygame.display.set_mode(img.get_size())


pygame.display.set_caption("Drag the mouse to draw!")
#create palette 
red_bar = pygame.Surface([40,40]).convert()
red_bar.fill((255, 0, 0))
green_bar = pygame.Surface([40,40]).convert()
green_bar.fill((0, 255, 0))
blue_bar = pygame.Surface([40,40]).convert()
blue_bar.fill((0, 0, 255))
pink_bar = pygame.Surface([40,40]).convert()
pink_bar.fill((255, 114, 86))

img = img.convert() #need to convert it after we have set-up the screen

#the display will not change, so we can blit & flip the display just once first
screen.blit(img, (0,0))
pygame.display.flip()

red = (255,0,0)
green =  (0, 255, 0)
blue = (0, 0, 255)
pink = ((255, 114, 86))
#variable for all colors 
colors = [red, green, blue, pink]

clock = pygame.time.Clock()
keep_going = True


prev_pos = (-1,-1)
#default is white 
colors = (255,255,255)
while keep_going:
    clock.tick(30)
        
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
    if pygame.mouse.get_pressed()[0]: #if left mouse is pressed
        x = ev.pos[0]  #the MOUSEBUTTONDOWN event has a position property
        y = ev.pos[1]  #that is an (x, y) tuple  
        if prev_pos == (-1,-1):
            #first point
            prev_pos = pygame.mouse.get_pos() 
            
          
        elif y >= 0 and y < 40 and x >= 0 and x < 40:
            if pygame.mouse.get_pressed()[0]: #if left mouse is pressed
                new_pos = pygame.mouse.get_pos()
                #set color for correct placement 
                colors = red

        elif y >= 40 and y < 80 and x >= 0 and x < 40:
            if pygame.mouse.get_pressed()[0]: #if left mouse is pressed
                new_pos = pygame.mouse.get_pos()
                colors = green

        elif y >= 80 and y < 120 and x >= 0 and x < 40:
            if pygame.mouse.get_pressed()[0]: #if left mouse is pressed
                new_pos = pygame.mouse.get_pos()
                colors = blue

        elif y >= 120 and y < 140 and x >= 0 and x < 40:
            if pygame.mouse.get_pressed()[0]: #if left mouse is pressed
                new_pos = pygame.mouse.get_pos()
                colors = pink 
              
        #draw in the remaining space 
        else:
            new_pos = pygame.mouse.get_pos()
            pygame.draw.line(img, (colors), prev_pos, new_pos) 
            prev_pos = new_pos

      
    else:
        prev_pos = (-1,-1)


      
    screen.blit(img, (0,0))
    screen.blit(red_bar, (0,0))
    screen.blit(green_bar, (0,40))
    screen.blit(blue_bar, (0,80))
    screen.blit(pink_bar, (0,120))
    pygame.display.flip()




