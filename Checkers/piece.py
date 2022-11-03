from turtle import *

class Piece:
    def __init__(self,location,color):
        self.color = color
        self.location = location
        self.piece = Turtle()
        self.piece.penup()
        self.piece.speed(0)
        self.piece.shape('circle')
        self.piece.shapesize(4,4)
        self.piece.goto(self.location)
        self.piece.color(self.color)
        self.isKing = False
        
    def getPos(self):
        return self.piece.pos()

    def move(self,location):
        self.piece.goto(location)
    
    def getColor(self):
        return self.piece.color()[0]

    def delete(self):
        self.piece.hideturtle()
        self.piece.reset()

class PossibleMove:
    def __init__(self,location):
        self.location = location
        self.possibleMove = Turtle()
        self.possibleMove.penup()
        self.possibleMove.speed(0)
        self.possibleMove.goto(location)
        self.possibleMove.shape('circle')
        self.possibleMove.color('green')
    
    def getPos(self):
        return self.possibleMove.pos()

    def delete(self):
        self.possibleMove.hideturtle()
        self.possibleMove.reset()
