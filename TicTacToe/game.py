class Location:
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Token:
    shape = ""
    location = Location(0,0)
    def __init__(self,x,y):
        self.location = Location(x,y)
        
    def getShape(self):
        self.shape

class Game:
    
    def __init__(self):
        pass

    def placeToken(self,token):
        pass