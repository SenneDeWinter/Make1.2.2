#!/usr/bin/env python
"""
Stel dat je een lijst met lijsten hebt waar elke waarde in de binnenste lijsten een tekenreeks is.
Je kunt het raster[x][y] zien als het karakter op de x- en y-coördinaten van een "plaatje" dat met tekstkarakters is
getekend. De (0, 0) oorsprong zal in de linkerbovenhoek liggen, de x-coördinaten nemen toe naar rechts, en de
y-coördinaten nemen toe naar beneden.
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def main():
    list = [['.', '.', '.', '.', '.', '.'],  #to make a list
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    print("Op welke manier wil je de lijst printen?") #to print this question
    print("1: 90 graden gedraaid")                    #to print the choices:
    print("2: 270 graden gedraaid")

    keuze = input("Geef je keuze in (1/2): \n")       #to prompt the user to make a decision

    if keuze == "1":                                  #to do something if the choice is 1
        for x in range(6):                            #to set the x coordinate
            for y in range(9):                        #to set the y coordinate
                if y < 8:                             #to do something if the y coordinate is smaller than 8
                    print(list[y][-(x + 1)], end="")  #to print the list
                else:
                    print(list[y][x])                 #to print the list

    if keuze == "2":                                  #to do something if the choice is 2
        for x in range(6):                            #to set the x coordinate
            for y in range(9):                        #to set the y coordinate
                if y < 8:                             #to do something if the y coordinate is smaller than 8
                    print(list[y][+x], end="")        #to print the list
                else:
                    print(list[y][x])                 #to print the list


if __name__ == '__main__':    #code to execute if called from command-line
    main()