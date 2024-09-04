
import pygame
from vector import *
from fish import *
from flock import *

# pygame setup
#initialiserer alle de nødvendige moduler, der kræves for at bruge Pygame. Pygame består af flere moduler, hver med sit eget formål, såsom grafik, lyd, inputhåndtering osv.
#pygame.init() returnerer funktionen to værdier: en tæller af hvor mange moduler, der blev initialiseret korrekt, og en tæller af hvor mange moduler, der mislykkedes i at initialisere.
pygame.init()
screen = pygame.display.set_mode((800, 600))


#opretter et objekt af typen Clock`-objekt, til at styre hvor lang tid der går mellem hver iteration i lykken.
clock = pygame.time.Clock()
running = True


pos = Vector(30,30)
spd = Vector(1,1)
f = Fish(pos,spd)
ff = Fish(Vector(60,60),Vector(1,1))
flock = Flock()
flock.addFish(f)
flock.addFish(ff)


while running:
    
    #Så spillet kan lukkes
    #Denne linje henter en liste over alle hændelser (events), som er sket siden sidste gang, løkken kørte. 
    for event in pygame.event.get():

        #Denne event sker typisk når vinduet lukkes
        if event.type == pygame.QUIT:
            running = False

    #Lav en baggrundsfarve
    screen.fill((0, 128, 255))

    #Her skal animationen være
    

    flock.updateFlock()
    flock.drawFlock(screen)

    

    #Flip, så vores tegning kommer på skærmen.
    pygame.display.flip()

    #60 frames pr sekund. Dvs løkken skal gentages 60 gange i sekundet.
    clock.tick(60)

pygame.quit()
