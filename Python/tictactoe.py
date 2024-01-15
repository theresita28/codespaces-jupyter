# With the Help/ Idea of the source https://www.python-lernen.de/tic-tac-toe-python-tutorial.htm
# Tic-Tac-toe game

# Anleitung des Spiels:

spielfeld = ["", "1", "2", "3", "4", "5","6", "7","8", "9"]


print("Tic-Tac-Toe")
spiel_aktiv = True

#Funktion Spielfeld ausgeben
def spielfeld_ausgeben():
    print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
    print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
    print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )



def spieler_eingabe():
    while True:
        spielzug = input("Bitte Feld eingeben: ")
        # vorzeitiges Spielende durch Spieler
        if spielzug == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")


while spiel_aktiv:
    # aktuelles Spielfeld ausgeben
    spielfeld_ausgeben()
    # Eingabe des aktiven Spielers
    spielzug = spieler_eingabe()
    print("Ausgewähltes Feld: " + str(spielzug))

