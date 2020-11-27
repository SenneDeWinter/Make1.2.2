#!/usr/bin/env python
"""
Demo flowcontrol
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def main():
    global getal
    lijst = []
    i = 0
    while i <= 8:
        try:
            getal = int(input("Geef een willekeurig getal:  "))
            i += 1

            for a in range(1):
                lijst.append(getal)
                print(lijst)

        except ValueError as err:
            print("Dit is geen getal ->", err)
            i = i


if __name__ == '__main__':    #code to execute if called from command-line
    main()