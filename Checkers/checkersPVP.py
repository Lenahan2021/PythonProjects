from turtle import *
import turtle
from piece import *

boardCoordinates = []
pieces = []
possibleMoves =[]
screen = 0
selectedPiece = False

redPlayerTurn = False

def initScreen():
    global screen
    HEIGHT = 800
    WIDTH = 800

    screen = turtle.Screen()

    screen.setup(HEIGHT+4, WIDTH+8)
    screen.setworldcoordinates(0,HEIGHT, WIDTH, 0)

    screen.update()


def drawBoard():
    drawer = Turtle()
    drawer.speed(0)
    drawer.shape('square')
    drawer.shapesize(5,5)
    drawer.penup()
    global boardCoordinates
    for i in range(8):
        rows = []
        for s in range(8):
            if (s+i) % 2 == 0:
                drawer.color('black')
            else:
                drawer.color('red')
            drawer.goto(100*s, 100*i)
            drawer.stamp()
            rows.append(drawer.pos())
        boardCoordinates.append(rows)

def createPieces():
    global boardCoordinates
    global pieces
    for i in range(0, len(boardCoordinates)):
        if i < 3 or i > 4:
            #adds the offset to the checker pieces
            if i % 2 == 0:
                for s in range(0,len(boardCoordinates[i]), 2):
                    if i < 3:
                        piece = Piece(boardCoordinates[i][s], 'red')
                    else:
                        piece = Piece(boardCoordinates[i][s], 'grey')
                    pieces.append(piece)
            else:
                for s in range(1, len(boardCoordinates[i]), 2):
                    if i < 3:
                        piece = Piece(boardCoordinates[i][s], 'red')
                    else:
                        piece = Piece(boardCoordinates[i][s], 'grey')
                    pieces.append(piece)

def makeKings():
    global pieces
    for i in pieces:
        if i.getColor() == 'red' and i.getPos()[1] == 700 and not i.isKing:
            i.isKing = True
        elif i.getColor() == 'grey' and i.getPos()[1] == 0 and not i.isKing:
            i.isKing = True

def jumping(piecesLocation, p):
    if p.piece.color()[0] == 'red' and redPlayerTurn:
        if (p.getPos()[0] + 100, p.getPos()[1] + 100) in piecesLocation and not ((p.getPos()[0] + 200, p.getPos()[1] + 200) in piecesLocation) and not (p.getPos()[0] + 200 > 700 or p.getPos()[1] + 200 > 700):
            for i in pieces:
                if (i.getPos() == (p.getPos()[0] + 100, p.getPos()[1] + 100) and (i.getColor() == 'grey')):
                    possibleMove = PossibleMove((p.getPos()[0] + 200, p.getPos()[1] + 200))
                    possibleMoves.append(possibleMove)
        if (p.getPos()[0] - 100, p.getPos()[1] + 100) in piecesLocation and not ((p.getPos()[0] - 200, p.getPos()[1] + 200) in piecesLocation) and not (p.getPos()[0] - 200 < 0 or p.getPos()[1] + 200 > 700):
            for i in pieces:
                if (i.getPos() == (p.getPos()[0] - 100, p.getPos()[1] + 100) and (i.getColor() == 'grey')):
                    possibleMove = PossibleMove((p.getPos()[0] - 200, p.getPos()[1] + 200))
                    possibleMoves.append(possibleMove)
        if p.isKing:
            if (p.getPos()[0] + 100, p.getPos()[1] - 100) in piecesLocation and not ((p.getPos()[0] + 200, p.getPos()[1] - 200) in piecesLocation) and not (p.getPos()[0] + 200 > 700 or p.getPos()[1] - 200 < 0):
                for i in pieces:
                    if (i.getPos() == (p.getPos()[0] + 100, p.getPos()[1] - 100) and (i.getColor() == 'grey')):
                        possibleMove = PossibleMove((p.getPos()[0] + 200, p.getPos()[1] - 200))
                        possibleMoves.append(possibleMove)
            if (p.getPos()[0] - 100, p.getPos()[1] - 100) in piecesLocation and not ((p.getPos()[0] - 200, p.getPos()[1] - 200) in piecesLocation) and not (p.getPos()[0] - 200 < 0 or p.getPos()[1] - 200 < 0):
                for i in pieces:
                    if (i.getPos() == (p.getPos()[0] - 100, p.getPos()[1] - 100) and (i.getColor() == 'grey')):
                        possibleMove = PossibleMove((p.getPos()[0] - 200, p.getPos()[1] - 200))
                        possibleMoves.append(possibleMove)
        return possibleMoves
    elif p.piece.color()[0] == 'grey'and not redPlayerTurn:
        if (p.getPos()[0] + 100, p.getPos()[1] - 100) in piecesLocation and not ((p.getPos()[0] + 200, p.getPos()[1] - 200) in piecesLocation) and not (p.getPos()[0] + 200 > 700 or p.getPos()[1] - 200 < 0):
            for i in pieces:
                if (i.getPos() == (p.getPos()[0] + 100, p.getPos()[1] - 100) and (i.getColor() == 'red')):
                    possibleMove = PossibleMove((p.getPos()[0] + 200, p.getPos()[1] - 200))
                    possibleMoves.append(possibleMove)
        if (p.getPos()[0] - 100, p.getPos()[1] - 100) in piecesLocation and not ((p.getPos()[0] - 200, p.getPos()[1] - 200) in piecesLocation) and not (p.getPos()[0] - 200 < 0 or p.getPos()[1] - 200 < 0):
            for i in pieces:
                if (i.getPos() == (p.getPos()[0] - 100, p.getPos()[1] - 100) and (i.getColor() == 'red')):
                    possibleMove = PossibleMove((p.getPos()[0] - 200, p.getPos()[1] - 200))
                    possibleMoves.append(possibleMove)
        if p.isKing:
            if (p.getPos()[0] + 100, p.getPos()[1] + 100) in piecesLocation and not ((p.getPos()[0] + 200, p.getPos()[1] + 200) in piecesLocation) and not (p.getPos()[0] + 200 > 700 or p.getPos()[1] + 200 > 700):
                for i in pieces:
                    if (i.getPos() == (p.getPos()[0] + 100, p.getPos()[1] + 100) and (i.getColor() == 'red')):
                        possibleMove = PossibleMove((p.getPos()[0] + 200, p.getPos()[1] + 200))
                        possibleMoves.append(possibleMove)
            if (p.getPos()[0] - 100, p.getPos()[1] + 100) in piecesLocation and not ((p.getPos()[0] - 200, p.getPos()[1] + 200) in piecesLocation) and not (p.getPos()[0] - 200 < 0 or p.getPos()[1] + 200 > 700):
                for i in pieces:
                    if (i.getPos() == (p.getPos()[0] - 100, p.getPos()[1] + 100) and (i.getColor() == 'red')):
                        possibleMove = PossibleMove((p.getPos()[0] - 200, p.getPos()[1] + 200))
                        possibleMoves.append(possibleMove)
    
        return possibleMoves

    return []


def makePossibleMoves(piecesLocation, p):
    global pieces
    if p.piece.color()[0] == 'red' and redPlayerTurn:
        possibleMoves = jumping(piecesLocation, p)
        if not (p.getPos()[0] - 100 < 0 or p.getPos()[1] + 100 > 700) and not ((p.getPos()[0] - 100, p.getPos()[1] + 100) in piecesLocation):
            possibleMove = PossibleMove((p.getPos()[0] - 100, p.getPos()[1] + 100))
            possibleMoves.append(possibleMove)
        if not (p.getPos()[0] + 100 > 700 or p.getPos()[1] + 100 > 700) and not ((p.getPos()[0] + 100, p.getPos()[1] + 100) in piecesLocation):
            possibleMove = PossibleMove((p.getPos()[0] + 100, p.getPos()[1] + 100))
            possibleMoves.append(possibleMove)
        #checks to see if the p selected is a king, if it is then add our two extra moves
        if p.isKing:
            if not (p.getPos()[0] - 100 < -1 or p.getPos()[1] - 100 < -1) and not ((p.getPos()[0] - 100, p.getPos()[1] - 100) in piecesLocation):
                possibleMove = PossibleMove((p.getPos()[0] - 100, p.getPos()[1] - 100))
                possibleMoves.append(possibleMove)
            if not (p.getPos()[0] + 100 > 700 or p.getPos()[1] - 100 < -1) and not ((p.getPos()[0] + 100, p.getPos()[1] - 100) in piecesLocation):
                possibleMove = PossibleMove((p.getPos()[0] + 100, p.getPos()[1] - 100))
                possibleMoves.append(possibleMove)
        return possibleMoves   

    elif p.piece.color()[0] == 'grey' and not redPlayerTurn:
        possibleMoves = jumping(piecesLocation, p)
        if not (p.getPos()[0] - 100 < 0 or p.getPos()[1] - 100 < -1)and not ((p.getPos()[0] - 100, p.getPos()[1] - 100) in piecesLocation):
            possibleMove = PossibleMove((p.getPos()[0] - 100, p.getPos()[1] - 100))
            possibleMoves.append(possibleMove)
        if not (p.getPos()[0] + 100 > 700  or p.getPos()[1] - 100 < -1) and not ((p.getPos()[0] + 100, p.getPos()[1] - 100) in piecesLocation):
            possibleMove = PossibleMove((p.getPos()[0] + 100, p.getPos()[1] - 100))
            possibleMoves.append(possibleMove)
        if p.isKing:
            if not (p.getPos()[0] - 100 < -1 or p.getPos()[1] + 100 > 700) and not ((p.getPos()[0] - 100, p.getPos()[1] + 100) in piecesLocation):
                possibleMove = PossibleMove((p.getPos()[0] - 100, p.getPos()[1] + 100))
                possibleMoves.append(possibleMove)
            if not (p.getPos()[0] + 100 > 700 or p.getPos()[1] + 100 > 700) and not ((p.getPos()[0] + 100, p.getPos()[1] + 100) in piecesLocation):
                possibleMove = PossibleMove((p.getPos()[0] + 100, p.getPos()[1] + 100))
                possibleMoves.append(possibleMove)
        
        return possibleMoves     

def deletePieceToJump(selectedPiece, movePiece):
    global pieces
    currentPos = selectedPiece.getPos()
    newPos = movePiece.getPos()
    jumpPieceX = (currentPos[0] + newPos[0]) /2
    jumpPieceY = (currentPos[1] + newPos[1]) /2
    jumpPieceLocation = (jumpPieceX, jumpPieceY)
    for i in pieces:
        if jumpPieceLocation == i.getPos():
            i.delete()

def movePiece(selectedPiece, possibleMoves, x, y):
    global redPlayerTurn
    for p in possibleMoves:
        if (x, y) == p.getPos():
            deletePieceToJump(selectedPiece, p)
            selectedPiece.move(p.getPos())
            makeKings()
            if redPlayerTurn:
                redPlayerTurn = False
            else:
                redPlayerTurn = True
    for p in possibleMoves:
        p.delete()
    possibleMoves.clear()
    selectedPiece = False
    return selectedPiece
    

def pieceMovement(x,y):
    global possibleMoves
    global selectedPiece
    global redPlayerTurn
    #https://stackoverflow.com/questions/8866046/python-round-up-integer-to-next-hundred
    roundedX = round(x/100) * 100
    roundedY = round(y/100) * 100

    #Selecting piece and adding possibleMoves
    if not selectedPiece:
        for i in pieces:
            if i.piece.pos() == (roundedX, roundedY):
                if i.getColor() == 'red' and redPlayerTurn:
                    selectedPiece = i
                    piecesLocation = []
                    #update piecesLocation
                    for p in pieces:
                        piecesLocation.append(p.getPos())
                    possibleMoves = makePossibleMoves(piecesLocation=piecesLocation, p=i)
                elif i.getColor() == 'grey' and not redPlayerTurn:
                    selectedPiece = i
                    piecesLocation = []
                    #update piecesLocation
                    for p in pieces:
                        piecesLocation.append(p.getPos())
                    possibleMoves = makePossibleMoves(piecesLocation=piecesLocation, p=i)
    else:
        if len(possibleMoves) > 0:
            selectedPiece = movePiece(selectedPiece, possibleMoves, roundedX, roundedY)
        else:
            selectedPiece = False

#setup screen
initScreen()

drawBoard()
createPieces()

#click input
screen.onscreenclick(pieceMovement)
turtle.mainloop()