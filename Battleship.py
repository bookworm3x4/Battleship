# Battleship.py
# A two-player game of battleship facilitated by Flask.
# Emmett Wald
# 15 Dec. 2018

# outline
'''
- import flask
- create game board, ships
- intro game
- set up game: place battleships
- run game: choose first player, player aims, game returns
  hit/miss/sink/already went there, updates board, next turn
- check and end when someone wins
'''

# import Flask
'''do the thing'''

# game boards
WIDTH, HEIGHT = 15, 15
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def toNum(letter):
    return ALPHABET.find(letter)

class Board:
    '''A class for an array that will store locations of ships,
    hits, and misses.'''
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.array = [[" "] * width] * height

def boardSetup():
    '''Initializes the four board instances that will be used for play.'''
    board0self = Board("0self", WIDTH, HEIGHT)
    board0opp =  Board("0opp", WIDTH, HEIGHT)
    board1self = Board("1self", WIDTH, HEIGHT)
    board1opp =  Board("1opp", WIDTH, HEIGHT)
    boards = ((board0self, board0opp),
              (board1self, board1opp))

def printBoards(player):
    '''Displays the two boards visible to a given player.'''
    
    self = boards[player][0]
    opp =  boards[player][1]

    boardWidth = WIDTH * 2 + 1

    def printLabels():
        '''prints letter labels for the columns'''
        print("   ", end="")
        for i in range(WIDTH):
            print(ALPHABET[i] + " ")
            
    def printBorder(char):
        '''prints a horizontal border'''
        print(" +" + char*boardWidth + "+")
        
    def printBoardFill(board):
        '''prints the "guts" of the board with row labels and
        info from the array'''
        for j in range(HEIGHT):
            print(" |" + " "*boardWidth + "|")
            print(i + "|", end=" ")
            for i in range(WIDTH):
                value = board.array[i][j]
                print(value +, end=" ")
            print("|")
        print(" |" + " "*boardWidth + "|")    

    # now let's do the actual printing
    printLabels()
    printBorder("-")
    printBoardFill(opp)
    printBorder("=")
    printBoardFill(self)
    printBorder("-")
    printLabels()

# ships
class Ship:
    '''Defines a class that will hold information about the size, location,
    owner, and amount of damage to a ship.

    attributes:
    - name
    - width
    - length
    - player ~ who the ship belongs to
    - p1, p2 ~ opposite corners describing the ship's location
    - size ~ total area of ship
    - hits ~ counts number of hits that have been scored on the ship
    - sunk ~ True if the ship has been sunk, False otherwise

    methods:
    - place ~ allows player to put the ship on their board, updates board array
    - hit ~ updates hit counter and checks whether ship has been sunk
    '''
    
    def __init__(self, name, width, length):
        self.name = name.capitalize()
        self.width = width
        self.length = length
        self.player = -1
        self.p1 = []
        self.p2 = []
        self.size = width * length
        self.hits = 0
        self.sunk = False

    def place(self):
        x1, y1 = -1, -1
        loc = input("Where do you want to place your " + self.name +
                    "?\n(Give start position as a letter-number combo, e.g., B7.)\n")
        p2options = []
        while x1 not in range(WIDTH) or y1 not in range(HEIGHT) or board[self.player][0].array[x1][y1] != " " or p2options == []:
            x1 = toNum(loc[0])
            y1 = int(loc[1:])
            p2options = [[x1+WIDTH, y1+HEIGHT],
                         [x1+WIDTH, y1-HEIGHT],
                         [x1-WIDTH, y1+HEIGHT],
                         [x1-WIDTH, y1-HEIGHT],
                         [x1+HEIGHT, y1+WIDTH],
                         [x1+HEIGHT, y1-WIDTH],
                         [x1-HEIGHT, y1+WIDTH],
                         [x1-HEIGHT, y1-WIDTH]]
            for i in p2options:
                for j in p2options:
                    if i == j:
                        p2options.remove(j)
            for point in p2options:
                x2, y2 = point
                if x2 not in range(WIDTH) or y2 not in range(HEIGHT) or board[self.player][0].array[x2][y2] != " ":
                    p2options.remove(point)
            if x1 not in range(WIDTH) or y1 not in range(HEIGHT):
                loc = input("That's not a valid location. Choose a location between A1 and " +
                            ALPHABET[WIDTH] + int(HEIGHT) + ".\n")
            elif board[self.player][0].array[x1][y1] != " ":
                loc = input("You already have a ship there. Choose a different spot.\n")
            else:
                loc = input("There's not enough room for that ship there.\nChoose a different spot.\n")
        self.p1 = [x1, y1]
        print("Okay, the starting point for your ship is " + ALPHABET[x1] + str([y1]) + ".")
        if len(p2options) == 1:
            self.p2 = p2options[0]
            print("The endpoint of your ship is " + ALPHABET[p2[0]] + str(p2[1]) + ".")
        else:
            print("You can place the endpoint of your " + self.name + " at any of the following points:", end="")
            for point in p2options:
                print(" " + ALPHABET[point][0] + str(point[1]), end="")
            print(".")
        loc2 = input("Where do you want to put it?\n")
        #check against list of p2options, then confirm                       
        #update self.p2
        #update array to reflect ship location

        def hit(self):
            self.hits += 1
            if self.hits == self.size:
                self.sunk = True
                return self.sunk

def createShips():
    '''Creates the ship objects that will be used for the game.'''
    ships = []
    for player in range(2):
        ships[player] = (Ship(carrier, 1, 5),
                         Ship(battleship, 1, 4),
                         Ship(destroyer, 1, 3),
                         Ship(submarine, 1, 3),
                         Ship(patrol, 1, 2))
    return ships
    
def placeShips():
    '''Asks each player to place their ships on the gameboard and
    stores the locations.'''

    for player in range(2):
        for i in range(len(ships[player])):
            ships[player][i].place()

def intro():
    print("Welcome to Battleship!")
    #introduce game and rules and ships and board

def main():

    # background stuff
    boardSetup()
    createShips()

    # game play
    intro()
    #randomly choose who goes 1st
    #turn: aim, check, return hit/miss/etc, check winner, change turn
    #end game
