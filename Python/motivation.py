# Motivation programm 
# With the Help/ Idea of the source https://www.python-lernen.de/uebung-lobesreden.htm

import random

adjektivlist = ["beste", "liebenswürdigste", "schönste", "größte"]
nomenlist = ["Mensch", "Programmierer", "Freund"] 


adjektiv = random.choice(adjektivlist)
nomen = random.choice(nomenlist)

print("Du bist der " + adjektiv + " " + nomen)