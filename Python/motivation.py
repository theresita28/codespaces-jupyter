# Motivation programm 
# With the Help/ Idea of the source https://www.python-lernen.de/uebung-lobesreden.htm
# Update: gendern mit chat api/ spacy
# In Blog ausführlicher erklären über gender probleme und mit den Adjektiven...

import random

gender = input("Bitte Geschlecht angeben(männlich, weiblich)")

adjektivlist = ["beste", "liebenswürdigste", "schönste", "größte"]
nomenlist = ["Mensch", "Programmierer", "Freund"]

adjektiv = random.choice(adjektivlist)
nomen = random.choice(nomenlist)

if gender == "männlich":

    print("Du bist der " + adjektiv + " " + nomen)
elif gender == "weiblich":
    if (nomen == "Programmierer"):
        nomen = "Programmierierin"
    
    if (nomen == "Freund"):
        nomen = "Freundin"

    print("Du bist die " + adjektiv + " " + nomen)
else:
    print("Falsche Eingabe: Bitte männlich oder weiblich eingeben")