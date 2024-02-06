# Inspiration https://www.python-lernen.de/pygame-animation.htm
# Importieren der Pygame-Bibliothek
import pygame, math

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

FENSTERBREITE = 640
FENSTERHÖHE = 480

# Fenster öffnen
screen = pygame.display.set_mode((FENSTERBREITE, FENSTERHÖHE))

# Titel für Fensterkopf
pygame.display.set_caption("Unser erstes Pygame-Spiel")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Definieren der Variablen
ballpos_x = 10
ballpos_y = 30

BALL_DURCHMESSER = 20

bewegung_x = 4
bewegung_y = 4

spielfigur_1_x = 20
spielfigur_1_y = 20
spielfigur_1_bewegung = 0

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
                spielfigur_1_bewegung = -6
            if event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
                spielfigur_1_bewegung = 6
    # Spiellogik hier integrieren
    if spielfigur_1_bewegung != 0:
        spielfigur_1_y += spielfigur_1_bewegung
    # Spielfeld löschen
    screen.fill(SCHWARZ)

    # Spielfeld/figuren zeichnen
    pygame.draw.ellipse(screen, WEISS,[ballpos_x,ballpos_y,BALL_DURCHMESSER,BALL_DURCHMESSER])
    # -- Spielerfigur 1
    pygame.draw.rect(screen, WEISS, [spielfigur_1_x, spielfigur_1_y, 20, 100])
    # bewegen unseres Kreises
    ballpos_x += bewegung_x
    ballpos_y += bewegung_y

    if ballpos_y > FENSTERHÖHE - BALL_DURCHMESSER or ballpos_y < 0:
        bewegung_y = bewegung_y * -1

    if ballpos_x > FENSTERBREITE - BALL_DURCHMESSER or ballpos_x < 0:
        bewegung_x = bewegung_x * -1

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()