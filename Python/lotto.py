#https://www.python-lernen.de/uebung-lotto-simulator.htm

#Lotto-Simulator: Gibt zufällig 6 Zahlen aus den Bereich 1-50 aus.

import random

zahlen = []

for i in range(0,49,1):
    zahlen.append(i+1)

gewinner = random.sample(zahlen, 6)


gewinner.sort()
print(gewinner)  