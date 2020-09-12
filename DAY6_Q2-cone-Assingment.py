import math

pi = math.pi

class cone:
    
    def __init__(self,r,h): 

        self.r=r
        
        self.h=h
        
    def volume(self):
        
        result = (1 / 3) * pi * self.r * self.r * self.h
        
        print("\nVolume Of Cone is :",result)
        
    def surfacearea(self):
        
        result = pi * self.r * self.h + pi * self.r * self.r
         
        print("\nSurface Area Of Cone is :",result)

ra = float(input("\nEnter the radius of cone : "))

he = float(input("\nEnter the height of cone : "))

c = cone( ra, he)

c.volume()

c.surfacearea()


