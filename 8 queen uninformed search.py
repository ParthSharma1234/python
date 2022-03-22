import numpy as np

# make a chessboard of 8x8 initially having no queen.
# 0 = queen absent at the block
# 1 = queen present

counter = 0


def isSafe(chess, row, col):
    # verify if row is safe
    for i in range(0, 8):
        if chess[row][i] == 1:
            return False

    diff = 0

    # verify if diagonals are safe
    while diff < 8:
        if row - diff > -1 and col - diff > -1 and chess[row - diff][col - diff] == 1 or \
                row - diff > -1 and col + diff < 8 and chess[row - diff][col + diff] == 1 or \
                row + diff < 8 and col - diff > -1 and chess[row + diff][col - diff] == 1 or \
                row + diff < 8 and col + diff < 8 and chess[row + diff][col + diff] == 1:
            return False

        diff += 1

    return True


def dfs(chess, curr_column):
    global counter

    if curr_column > 7:
        return

    for row in range(0, 8):
        counter += 1

        # clearing the previous row
        clr = row
        while clr > -1:
            chess[clr][curr_column] = 0
            clr -= 1

        # print ('row, col', row, curr_column)
        if isSafe(chess, row, curr_column):
            chess[row][curr_column] = 1
            if curr_column == 7:
                print('moves:', counter)
                print(chess)

            dfs(chess, curr_column + 1)


if __name__ == "__main__":
    # Creating an empty chess board
    chess = np.full((8, 8), 0)

    # start putting queens one by one
    dfs(chess, 0)