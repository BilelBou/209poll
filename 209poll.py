#!/usr/bin/env python3 
## Math
## File description:
## By Bilel Bouricha
##

import sys
from math import sqrt


def help():
    print("USAGE\n"
          "\t./209poll pSize sSize p\n\n"
          "DESCRIPTION\n"
          "\tpSize\tsize of the population\n"
          "\tsSize\tsize of the sample (supposed to be representative)\n"
          "\tp\tpercentage of voting intentions for a specic candidate", end="")
def variance(pSize, sSize, p):
    pp = p / 100
    var = (pp * (1 - pp) / sSize) * ((pSize - sSize) / (pSize - 1))
    return var

def check_min(nb):
    if nb < 0:
        return (0)
    else:
        return nb

def check_max(nb):
    if nb > 100:
        return (100)
    else:
        return nb

def exec():
    try:
        pSize = int(sys.argv[1])
        sSize = int(sys.argv[2])
    except:
        exit(84)
    try:
        p = float(sys.argv[3])
    except:
        exit(84)
    var = variance(pSize, sSize, p)
    p1 = (2 * 1.96 * sqrt(var)) / 2 * 100
    p2 = (2 * 2.58 * sqrt(var)) / 2 * 100
    print("Population size:\t\t{}".format(pSize))
    print("Sample size:\t\t\t{}".format(sSize))
    print("Voting intentions:\t\t{0:.2f}%".format(p))
    print("Variance:\t\t\t{0:.3}".format(var))
    print("95% confidence interval:\t[{0:.2f}%; {1:.2f}%]".format(check_min(p - p1), check_max(p + p1)))
    print("99% confidence interval:\t[{0:.2f}%; {1:.2f}%]".format(check_min(p - p2), check_max(p + p2)))

if (__name__ == '__main__'):
    if len(sys.argv) > 1 and sys.argv[1] == "-h":
        help()
    if len(sys.argv) != 4:
        exit(84)
    exec()