import numpy as np
import pandas as pd

# 4 by 4 board

# board = np.array(
#     [[0, 2, 0, 2],
#     [" ", 0, " ", 0],
#     [0, " ", 0, " ",],
#     [1, 0, 1, 0]]
# )

# 6 by 6 board

# board = np.array(
#     [[0, 2, 0, 2, 0, 2],
#      [2, 0, 2, 0, 2, 0],
#      [0, " ", 0, " ", 0, " "],
#      [" ", 0, " ", 0, " ", 0],
#      [0, 1, 0, 1, 0, 1],
#      [1, 0, 1, 0, 1, 0]]
# )

# 8 by 8 board

board = np.array(
    [[0, 2, 0, 2, 0, 2, 0, 2],
     [2, 0, 2, 0, 2, 0, 2, 0],
     [0, 2, 0, 2, 0, 2, 0, 2],
     [" ", 0, " ", 0, " ", 0, " ", 0],
     [0, " ", 0, " ", 0, " ", 0, " "],
     [1, 0, 1, 0, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0]]
)

boardSize = len(board[0])


def printBoard(board):
    sp = ' ' * 3
    refrence_line = ""
    for i in range(boardSize):
        refrence_line += sp + f"{i}"
    print("\n"+refrence_line)
    print(board)
    print(refrence_line)


def select(row0, col0):
    if (-1 < row0 < boardSize) and (-1 < col0 < boardSize):
        return row0, col0
    return False


def isSpaceFree(row, col):
    return board[row][col] == " "


def beating1(row, col, row0, col0, ur_le):
    return row - row0 == -2 and abs(col - col0) == 2 and board[(row + row0) // 2][(col + col0) // 2] == str(ur_le)


def beating2(row, col, row0, col0, ur_le):
    return row - row0 == 2 and abs(col - col0) == 2 and board[(row + row0) // 2][(col + col0) // 2] == str(ur_le)


def validMove1(row, col, row0, col0):
    prev = select(row0, col0)
    if board[row0][col0] == "1":
        if beating1(row, col, row0, col0, 2) and is_king1(row, col):
            return "beating and king"
        elif beating1(row, col, row0, col0, 2):
            return "beating"
        elif is_king1(row, col):
            return "king"
        return row == prev[0] - 1 and abs(col - prev[1]) == 1
    elif board[row0][col0] == "k1":
        if (board[(row + row0) // 2][(col + col0) // 2] == "2" or board[(row + row0) // 2][
                (col + col0) // 2] == "k2") and abs(row - prev[0]) == 2 and abs(col - prev[1]) == 2:
            return "king beating"
        if abs(row - prev[0]) == 1 and abs(col - prev[1]) == 1:
            return "king move"


def validMove2(row, col, row0, col0):
    prev = select(row0, col0)
    if board[row0][col0] == "2":
        if beating2(row, col, row0, col0, 1) and is_king2(row, col):
            return "beating and king"
        elif beating2(row, col, row0, col0, 1):
            return "beating"
        elif is_king2(row, col):
            return "king"
        return row == prev[0] + 1 and abs(col - prev[1]) == 1
    elif board[row0][col0] == "k2":
        if (board[(row + row0) // 2][(col + col0) // 2] == "1" or board[(row + row0) // 2][
                (col + col0) // 2] == "k1") and abs(row - prev[0]) == 2 and abs(col - prev[1]) == 2:
            return "king beating"
        if abs(row - prev[0]) == 1 and abs(col - prev[1]) == 1:
            return "king move"


def player1move(row, col, row0, col0):
    if bool(validMove1(row, col, row0, col0)):
        if validMove1(row, col, row0, col0) == "beating and king" or validMove1(row, col, row0, col0) == "king beating":
            board[row][col] = "k1"
            board[(row + row0) // 2][(col + col0) // 2] = " "
        elif validMove1(row, col, row0, col0) == "beating":
            board[row][col] = 1
            board[(row + row0) // 2][(col + col0) // 2] = " "
        elif validMove1(row, col, row0, col0) == "king" or validMove1(row, col, row0, col0) == "king move":
            board[row][col] = "k1"
        elif validMove1(row, col, row0, col0):
            board[row][col] = 1
        board[row0][col0] = " "
    else:
        return "Invalid move!!"


def player2move(row, col, row0, col0):
    if bool(validMove2(row, col, row0, col0)):
        if validMove2(row, col, row0, col0) == "beating and king" or validMove2(row, col, row0, col0) == "king beating":
            board[row][col] = "k2"
            board[(row + row0) // 2][(col + col0) // 2] = " "
        elif validMove2(row, col, row0, col0) == "beating":
            board[row][col] = 2
            board[(row + row0) // 2][(col + col0) // 2] = " "
        elif validMove2(row, col, row0, col0) == "king" or validMove2(row, col, row0, col0) == "king move":
            board[row][col] = "k2"
        elif validMove2(row, col, row0, col0):
            board[row][col] = 2
        board[row0][col0] = " "
    else:
        return "Invalid move!!"


def is_king1(row, col):
    return row == 0 and col in [2 * jule + 1 for jule in range(boardSize // 2)]


def is_king2(row, col):
    return row == boardSize - 1 and col in [2 * jule for jule in range(boardSize // 2)]


def main():
    Player1 = input("\nEnter your name Player1: ")
    Player2 = input("\nEnter your name Player2: ")
    printBoard(board)
    while True:

        while True:
            try:
                row0 = input("\n" + f"enter initial row {Player1}: ")
                if row0 == "again":
                    break
                row0 = int(row0)
                col0 = int(input(f"enter initial column {Player1}: "))
                if board[row0][col0] != "1" and board[row0][col0] != "k1":
                    print("box does not contain your piece")
                    continue
                row = int(input(f"enter the row on the board {Player1}: "))
                col = int(input(f"enter the column on the board {Player1}: "))
                if not((-1) ** row == (-1) ** col):
                    if isSpaceFree(row, col):
                        if player1move(row, col, row0, col0) == "Invalid move!!":
                            print("Invalid move!!")
                            continue
                    else:
                        print("Space is not free!!")
                        continue
                else:
                    print("Its a False Box!!")
                    continue
                player1move(row, col, row0, col0)
                break
            except:
                print("Invalid input!!")
                continue
        printBoard(board)

        if np.count_nonzero(board == "2") == 0 and np.count_nonzero(board == "k2") == 0:
            print(f"{Player1} wins")
            break

        while True:
            try:
                row0 = input("\n"+f"enter initial row {Player2}: ")
                if row0 == "again":
                    break
                row0 = int(row0)
                col0 = int(input(f"enter initial column {Player2}: "))
                if board[row0][col0] != "2" and board[row0][col0] != "k2":
                    print("box does not contain your peice")
                    continue
                row = int(input(f"enter the row on the board {Player2}: "))
                col = int(input(f"enter the column on the board {Player2}: "))
                if not ((-1) ** row == (-1) ** col):
                    if isSpaceFree(row, col):
                        if player2move(row, col, row0, col0) == "Invalid move!!":
                            print("Invalid move!!")
                            continue
                    else:
                        print("Space is not free!!")
                        continue
                else:
                    print("Its a False Box!!")
                    continue
                player2move(row, col, row0, col0)
                break
            except:
                print("Invalid input!!")
                continue
        printBoard(board)

        if np.count_nonzero(board == "1") == 0 and np.count_nonzero(board == "k1") == 0:
            print(f"{Player2} wins")
            break


def initiate():

    print("team checkers is glad to see you playing this game :)\n")
    print("This game has a limit. Game will only end when peices of your opponents are zero and there is no draw.\n")
    print("To hope over multiple peices at a time you have to first hope over the first peice and then type again and hope over the left peices.\n")
    intention = input("Do you want to continue (Y/N): ")
    if intention.lower() == "y":
        start = pd.Timestamp.now()
        main()
        print(pd.Timestamp.now() - start)
    print(f"Thank you :)")


initiate()
