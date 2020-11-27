#!/usr/bin/env python
"""
een script waarbij je om input vraagt achter een willekeurig woord en waarbij het script het woord achterstevoren
weergeeft.
"""


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Production"


def main():
    invoer = str(input("Vul een woord of zin in \n"))  #to prompt the user for an input, to start a new line
    lengte = len(invoer)                               #to determine the length of the input
    achterstevoren = invoer[lengte::-1]                #to put the input backwards
    print(achterstevoren)                              #to print the input backwards


if __name__ == '__main__':    #code to execute if called from command-line
    main()