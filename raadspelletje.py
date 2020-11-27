#!/usr/bin/env python
"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
De lijst mag je kiezen:

    ofwel uit een bestand lezen
    ofwel zelf een lijst samenstellen in je script
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def main():
    lijst = ["IoT", "bij", "KdG", "is", "veel", "beter", "dan", "bij", "AP", "#signthepetition"] #to make a list

    raden = input("Geef een woord in om te raden of het in de lijst staat  ") #to ask for an input

    while True:
        if raden in lijst:                                     #to check if the input is in the list
            print("Het woord staat in de lijst!!")             #to print a message when the word is in the list
            break                                              #to stop the program
        else:                                                  #to do something if the word isn't in the list
            print("Helaas, het woord staat niet in de lijst")  #to print that the word isn't in the list
            break                                              #to stop the program


if __name__ == '__main__':    #code to execute if called from command-line
    main()