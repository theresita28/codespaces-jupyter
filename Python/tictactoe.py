# With the Help/ Idea of the source https://www.python-lernen.de/tic-tac-toe-python-tutorial.htm
# Tic-Tac-toe game

# Anleitung des Spiels:

spielfeld = ["", "1", "2", "3", "4", "5","6", "7","8", "9"]


print("Tic-Tac-Toe")

#Funktion Spielfeld ausgeben
def spielfeld_ausgeben():
    print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
    print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
    print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )

spielfeld_ausgeben()