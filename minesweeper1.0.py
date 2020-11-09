import pygame
import numpy

pygame.init()
pygame.font.init()

display_width = 820
display_height = 820

width = 10
height = 10
bombs = 12
font = pygame.font.SysFont('Comic Sans MS', 25)

bombsarray = numpy.zeros(shape=(width,height), dtype=str)
bombcountarray = numpy.zeros(shape=(width,height), dtype=int)

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

def generateBombs(bmbs):
    for i in range(bmbs):
        x = numpy.random.randint(low=1,high=9)
        y = numpy.random.randint(low=1,high=9)
        bombsarray[x,y] = 'x'

    for x in range(width):
        for y in range(height):
            if bombsarray[x,y] != 'x':
                bombsarray[x,y] = ' '

    for x in range(1,9):
        for y in range(1,9):
            if bombsarray[x,y] != 'x':
                for i in [x-1,x,x+1]:
                    for j in [y-1,y,y+1]:
                        if bombsarray[i,j] == 'x':
                            print(i,j)
                            bombcountarray[x,y] += 1
            
    for x in range(width):
        for y in range(height):
            if bombsarray[x,y] != 'x':
                bombsarray[x,y] = bombcountarray[x,y]
    print(bombsarray)
    print(bombcountarray)

def drawText(x,y,text,color):
    textsurface = font.render(text, False, color)
    gameDisplay.blit(textsurface,(x,y))
    
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pepo')
clock = pygame.time.Clock()

generateBombs(bombs)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    
    for x in range(1,9):
        for y in range(1,9):
            if bombsarray[x,y] == 'x':
                drawText(((x-1)*100)+50,((y-1)*100)+50,bombsarray[x,y], red)
            else:
                drawText(((x-1)*100)+50,((y-1)*100)+50,bombsarray[x,y], white)

    pygame.display.update()
    clock.tick(60)





pygame.quit()
quit()
