# Jeremy Whittier

# Initialize the board
board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

# Identify the various positions

pos1 = board[0][0]
pos2 = board[0][1]
pos3 = board[0][2]
pos4 = board[1][0]
pos5 = board[1][1]
pos6 = board[1][2]
pos7 = board[2][0]
pos8 = board[2][1]
pos9 = board[2][2]

test1board = [["X", "X", "X"], ["O", "O", "O"], ["X", "X", "X"]]
numboard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
loseboard = [["X", "O", "O"], ["O", "X", "X"], ["X", "X", "O"]]

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
    for row in board:
        if row[0] == row[1] == row[2]:
            return 1

# Check for diagonal matches
    if board[0][0] == board[1][1] == board[2][2]:
        return 1
    elif board[0][2] == board[1][1] == board[2][0]:
        return 1

    return 0
def wincheck(player, board):
    if winmatch(board) == 1:
        print("Yay! " + player)
    else:
        print("nop")

#printboard(board)
printboard(numboard)
winmatch(numboard)
winmatch(board)

wincheck(player1,board)

fancyprint(numboard)
