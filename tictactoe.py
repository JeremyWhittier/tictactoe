# Jeremy Whittier

# Initialize the board
gameboard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

# Identify the various positions


test1board = [["X", "X", "X"], ["O", "O", "O"], ["X", "X", "X"]]
vert0board = [["X", "O", "X"], ["X", "O", "O"], ["X", "X", "O"]]
numboard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
loseboard = [["X", "O", "O"], ["O", "X", "X"], ["X", "X", "O"]]
startingboard = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

player1 = "jeremy"
player2 = "ashley"

def printboard(playerboard):
    for line in playerboard:
        print(line)


def fancyprint(board):
    for counter, row in enumerate(board):
        if counter == 1 or counter == 2:
            print("----------")
        print(row[0] + " | " + row[1] + " | " + row[2])


def winmatch(board):
    """
    Used to check if board has a winner
    """
# Check for horizontal row matches
    for row in board:
        if row[0] == row[1] == row[2]:
            return 1

# Check for vertical column matches
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i]:
            return 1

# Check for diagonal matches
    if board[0][0] == board[1][1] == board[2][2]:
        return 1
    elif board[0][2] == board[1][1] == board[2][0]:
        return 1

    return 0


def wincheck(board):
    if winmatch(board) == 1:
#        print("Yay! ")
        return True
    else:
#        print("nop")
        return False


def wanttoplay():
    print("Do you want to play?")
    response = input("Enter yes or no: ")
    response = response.lower()
    if response == "yes" or response == "y":
        startgame()
    else:
        print("Maybe nextime")
        quit()


def startgame():
    turn = 0
    print("You are a winner just for playing!\n")
    while wincheck(gameboard) is False:
        if turn == 0:
            print("Alright, X is up first.\n")
            makeamove(gameboard, "X")
        elif turn % 2 == 1:
            print("O, you are up!\n")
            makeamove(gameboard, "O")
        elif turn % 2 == 0:
            print("X, your turn again!\n")
            makeamove(gameboard, "X")
        turn += 1
    print("\n+++++++++++++++++++++")
    print("We have a winner!!!")
    fancyprint(gameboard)


def makeamove(gameboard, xo):

    print("Hello " + xo + ", Here are the positions numbers:\n")
    fancyprint(numboard)
    print("\nHere is what the board currently looks like")
    fancyprint(gameboard)
    pospicked = input("\n Player " + xo + ", What position do you choose?")
    placemove(gameboard, pospicked, xo)

def placemove(gameboard, pospicked, xo):
#TODO Ask Sr. Saunderos how to do this:
#    pos1 = gameboard[0][0]
#    pos2 = gameboard[0][1]
#    pos3 = gameboard[0][2]
#    pos4 = gameboard[1][0]
#    pos5 = gameboard[1][1]
#    pos6 = gameboard[1][2]
#    pos7 = gameboard[2][0]
#    pos8 = gameboard[2][1]
#    pos9 = gameboard[2][2]

    pospicked = int(pospicked)

    if pospicked == 1:
        gameboard[0][0] = xo
    elif pospicked == 2:
        gameboard[0][1] = xo
    elif pospicked == 3:
        gameboard[0][2] = xo
    elif pospicked == 4:
        gameboard[1][0] = xo
    elif pospicked == 5:
        gameboard[1][1] = xo
    elif pospicked == 6:
        gameboard[1][2] = xo
    elif pospicked == 7:
        gameboard[2][0] = xo
    elif pospicked == 8:
        gameboard[2][1] = xo
    elif pospicked == 9:
        gameboard[2][2] = xo
    else:
        print("Gosh, that doesn't seem right")
    return gameboard


# printboard(board)
# printboard(numboard)
# winmatch(numboard)
# winmatch(board)
# wincheck(player1,board)
# winmatch(vert0board)
# fancyprint(numboard)

wanttoplay()
