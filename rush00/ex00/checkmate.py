#!/usr/bin/env python3
pieces = ['.', 'P', 'R', 'B', 'Q', 'K']

#core checkmate method
def checkmate(board):
    try:
        #print(board)
        boardArr = BoardStringToArray(board)
        kingPos = ValidatePiece(boardArr)
        
        if (IsKingThreated(boardArr, kingPos)):
            print("Success")
        else:
            print("Fail")  
              
        # print(boardArr)
        # print(kingPos)
        
    except Exception as e:
        print(f"Error: {e}")

#Turn board string into array and checking for incorrect condition
#i.e. Empty input, Bigger than 8,Not a square
#input: String board
#return: char[][] boardArr
def BoardStringToArray(board):
        #check does board is a instance of string
        if (not isinstance(board, str)):
            raise Exception("Board is not a string")
        
        #clean board string and turn into array     
        lines = []
        for line in board.strip().split('\n'):
            cleaned = line.strip().upper()
            if (len(cleaned) > 0): lines.append(cleaned) 
        
        #Check for empty board
        if (len(lines) == 0):
            raise Exception("Empty input")
       
        #Check if it's size bigger that 8 
        if (len(lines) > 8) :
            raise Exception("Cannot proceed a square bigger than 8")
        
        #Check does it's a square 
        for line in lines:
            if len(line) != len(lines):
                raise Exception("Not a square")

        #Turn into 2D board array
        boardArr = []
        for line in lines:
            lineArr = list(line)
            boardArr.append(lineArr)
       
        return boardArr

#Validate piece condition i.e. multiple King, No king, Turn not in used character in to empty cell and return King's Pos
#input: char[][] boardArr
#return: int[] kingPos
def ValidatePiece(boardArr):
    kCounter = 0
    qCounter = 0
    rCounter = 0
    bCounter = 0
    pCounter = 0
    kingPos = [] 
    for i in range(len(boardArr)):
        for j in range(len(boardArr[i])):
            element = boardArr[i][j]
            
            #turn not in used character in to empty cell
            if element not in pieces:
               boardArr[i][j] = '.'
            
            if element == 'K':
                kCounter += 1
                #King's position [row, col]
                kingPos = [i, j]
            if element == 'Q':
                qCounter += 1
            if element == 'R':
                rCounter += 1
            if element == 'B':
                bCounter += 1
            if element == 'P':
                pCounter += 1
   
    #check for multiple King 
    if kCounter > 1:
        raise Exception("More than one King")
    if qCounter > 1:
        raise Exception("More than one Queen")
    if rCounter > 2:
        raise Exception("More than two Rooks")
    if bCounter > 2:
        raise Exception("More than two Bishops")
    if pCounter > 8:
        raise Exception("More than eight Pawns")
    
    #check does board have no King
    if kCounter == 0:
        raise Exception("There is no King")
    
    return kingPos

#Check does King get checked
#input: char[][] boardArr, int[] kingPos 
#return: boolean
def IsKingThreated(boardArr, kingPos):
    kingRow = kingPos[0]
    kingCol = kingPos[1]

    #Check for straight line threat (Rook and Queen)
    straightThreat = ['R', 'Q']
    #Find threat Up, Down, Left, Right in Order
    if (CheckDirection(kingRow, kingCol, -1, 0, boardArr, straightThreat) or 
        CheckDirection(kingRow, kingCol, 1, 0, boardArr, straightThreat) or
        CheckDirection(kingRow, kingCol, 0, 1, boardArr, straightThreat) or 
        CheckDirection(kingRow, kingCol, 0, -1, boardArr, straightThreat)): 
        return True
    
    #check for diagonal threat (Bishop and Queen)
    diagonalThreat = ['B', 'Q']
    #Find threat UpLeft, UpRight, DownLeft, DownRight in Order
    if (CheckDirection(kingRow, kingCol, -1, -1, boardArr, diagonalThreat) or 
        CheckDirection(kingRow, kingCol, -1, 1, boardArr, diagonalThreat) or
        CheckDirection(kingRow, kingCol, 1, -1, boardArr, diagonalThreat) or 
        CheckDirection(kingRow, kingCol, 1, 1, boardArr, diagonalThreat)): 
        return True

    #check for pawn threat and pawn can move UpLeft and UpRight
    #so move DownLeft and DownRight from Queen to find pawn threat
    pawnDownLeft= [1, -1]
    pawnDownRight = [1, 1]
    if (PawnThreatCheck(kingRow, kingCol, boardArr, pawnDownLeft) or
        PawnThreatCheck(kingRow, kingCol, boardArr, pawnDownRight)):
        return True
    
    return False

#Check threat direction by move row and col using deltaRow, deltaCol to face possible threat used for Rook, Bishop, Queen
#input : int kingRow, int kingCol, int deltaRow, int deltaCol, char[][] boardArr, char[] threats
#return: boolean
def CheckDirection(kingRow, kingCol, deltaRow, deltaCol, boardArr, threats):
    size = len(boardArr)
    #initial moving
    row = kingRow + deltaRow
    col = kingCol + deltaCol
    
    while (0 <= row < size) and (0 <= col < size):
        piece = boardArr[row][col]
        #facing a threat
        if piece in threats:
            return True
        
        #check does get block by another unspecific threat
        if piece != '.' :
            return False
        
        row += deltaRow
        col += deltaCol
    
    #not find any threat 
    return False

#look for Pawn threat
#input: int kingRow, int kingCol
def PawnThreatCheck(kingRow, kingCol, boardArr, pawnPos):
    size = len(boardArr)
    row = kingRow + pawnPos[0]
    col = kingCol + pawnPos[1]
    
    if (0 <= row < size) and (0 <= col < size):
        if boardArr[row][col] == 'P':
            return True
    return False
