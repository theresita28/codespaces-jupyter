# With the Help/ Idea of the source https://www.python-lernen.de/tic-tac-toe-python-tutorial.htm
# Tic-Tac-toe game

# Anleitung des Spiels:

spielfeld = ["", "1", "2", "3", "4", "5","6", "7","8", "9"]


print("Tic-Tac-Toe")
spiel_aktiv = True
spieler_aktuell = 'X'

#Funktion Spielfeld ausgeben
def spielfeld_ausgeben():
    print (spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3] )
    print (spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6] )
    print (spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9] )



def spieler_eingabe():
    global spiel_aktiv
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

def spieler_wechseln():
    global spieler_aktuell2
    if spieler_aktuell == 'X':
        spieler_aktuell = 'O'
    else:
        spieler_aktuell = 'X'

spielfeld_ausgeben()
while spiel_aktiv:
    
    
    # Eingabe des aktiven Spielers
    print ("Spieler " + spieler_aktuell + " am Zug")
    spielzug = spieler_eingabe()
    if spielzug:
        spielfeld[spielzug] = 'X'
        # aktuelles Spielfeld ausgeben
        spielfeld_ausgeben()
        spieler_wechseln()
    

