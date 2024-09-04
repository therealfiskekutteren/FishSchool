from fish import *

class Flock:

    def __init__(self):
        self.__fish = []

    def addFish(self,fish):
        self.__fish.append(fish)
    
    def updateFlock(self):
        for i in range(len(self.__fish)):
            self.__fish[i].update()
    def drawFlock(self,screen):
        for i in range(len(self.__fish)):
            self.__fish[i].draw(screen)
        
