import pygame

class Vector:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    def dotProduct(self,v2):
        return self.x*v2.x+self.y*v2.y

    def scalarProduct(self,k):
        return Vector(k*self.x,k*self.y)

    def print(self,text=""):
        print(text+"(" + str(self.x) + "," + str(self.y) + ")")
    
    def __str__(self):
        return print(self)
    
    def __add__(self,v2):
        return addV(self,v2)
    def __sub__(self,v2):
        return subV(self,v2)
    def __mul__(self,k):
        self.scalarProduct(k)



def addV(v1,v2):
    return Vector(v1.x+v2.x,v1.y+v2.y)

def subV(v1,v2):
    return addV(v1,v2.scalarProduct(-1))     

v1 = Vector(3,6)
v2 = Vector(4,2)


v1.print("v1:")
v2.print("v2:")
addV(v1,v2).print("v1+v2:")
print(v1.dotProduct(v2))
subV(v1,v2).print("v1-v2:")
(v1+v2).print("v1+v2:")
#(v1*3).print("v1*3")