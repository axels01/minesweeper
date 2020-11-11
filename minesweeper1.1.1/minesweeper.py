import sys
import numpy
import pygame

pygame.init()

#debug print options
numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(linewidth=300)
numpy.get_printoptions()['linewidth']

#width with a buffer of 2, a 8x8 game is width 10 and height 10
gameWidth = 12
gameHeight = 12
bombs = 18
squareSize = 30

#colours
black = (0,0,0)
white = (255,255,255)

#Textures
hidden = pygame.image.load("hidden.png")
flag = pygame.image.load("flag.png")
hiddenRect = hidden.get_rect()
flagRect = flag.get_rect()



#A string array, X for bombs and a number to be displayed
bombArray = numpy.full(shape=(gameWidth,gameHeight), dtype=str, fill_value='0')
#String array to keep track of the textures & flags
    #H Hidden
    #F Flag
    #O Open
flagArray = numpy.full(shape=(gameWidth,gameHeight), dtype=str, fill_value='H')

#Generation function
def generateBombs(bombs_count):
    #Generates the bombs at random x and y within the buffer of two
    for i in range(bombs_count):
        x = numpy.random.randint(low=1,high=(gameWidth - 1))
        y = numpy.random.randint(low=1,high=(gameHeight - 1))
        bombArray[x,y] = 'X'
    #Goes through the whole array except the buffer
    for x in range(1, gameWidth - 1):
        for y in range(1, gameHeight - 1):
            #If there is no bomb "X"
            #count always starts at zero for each "cell" in array
            if bombArray[x,y] != 'X':
                count = 0
                #Goes through the 3x3 "square" surrounding the current "cell"
                for i in [x-1, x, x+1]:
                    for j in [y-1, y, y+1]:
                        #Adds to and sets "count" of bombs in the looked at 3x3 square
                        if bombArray[i,j] == 'X':
                            count += 1
                            bombArray[x,y] = count

def draw(xPos, yPos, texture):
    gameDisplay.blit(texture, (xPos,yPos))
    print(xPos,yPos)

def drawSquares():
    for x in range(1, gameWidth - 1):
        for y in range(1, gameHeight - 1):
            locationX = (x-1)*squareSize
            locationY = (y-1)*squareSize
            
            if flagArray[x,y] == 'H':
                draw(locationX,locationY,hidden)
            if flagArray[x,y] == 'F':
                draw(locationX,locationY,flag)
    
def setDisplaySize(x,y):
    gameDisplay = pygame.display.set_mode((x,y))


def click(pos):
    for x in range(1, gameWidth - 1):
        for y in range(1, gameHeight - 1):
            square = Rect((x-1)*squareSize,(y-1)*squareSize,squareSize,squareSize)
            if square.contains(pos):
                flagArray[x,y] == 'O'
    

gameDisplay = pygame.display.set_mode((5,5))

setDisplaySize((gameWidth-2)*squareSize,(gameHeight-2)*squareSize)
clock = pygame.time.Clock()
generateBombs(bombs)
drawSquares()
print(bombArray)
print(flagRect)

hidden.convert()
flag.convert()

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click(pygame.mouse.get_pos())
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
