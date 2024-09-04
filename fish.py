import pygame

print("fish loaded")

class Fish:

    def __init__(self,pos,vel):
        self.__pos = pos
        self.__vel = vel
        self.fish_img = pygame.image.load('fish.jpg')
        self.fish_img = pygame.transform.scale(self.fish_img,(50,50))
    
    def draw(self,screen):
        screen.blit(self.fish_img,(self.__pos.x,self.__pos.y))

    def update(self):
        self.__pos += self.__vel
    