import numpy
import sys

numpy.set_printoptions(threshold=sys.maxsize)
numpy.set_printoptions(linewidth=300)
numpy.get_printoptions()['linewidth']

game_width = 12
game_height = 12
bombs = 18

bombarray = numpy.full(shape=(game_width,game_height), dtype=str, fill_value='0')


def generateBombs(bombs_count):
    for i in range(bombs_count):
        x = numpy.random.randint(low=1,high=(game_width - 1))
        y = numpy.random.randint(low=1,high=(game_height - 1))
        bombarray[x,y] = 'x'

    for x in range(1, game_width - 1):
        for y in range(1, game_height - 1):
            if bombarray[x,y] != 'x':
                count = 0
                for i in [x-1, x, x+1]:
                    for j in [y-1, y, y+1]:
                        if bombarray[i,j] == 'x':
                            count += 1
                            bombarray[x,y] = count
        



generateBombs(bombs)
print(bombarray)
