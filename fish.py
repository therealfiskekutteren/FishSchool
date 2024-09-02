from Main import *
import pygame

print("fish loaded")

class Fish:

    def __init__(self,pos,vel):
        self.__pos = pos
        self.__vel = vel
    
    def draw(screen):
        screen.blit(fish_img,(pos.x,pos.y))

    def update(self):
        self.__pos += self.__vel