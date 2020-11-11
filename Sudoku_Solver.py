# Solving Sudoku using Backtracking Algorithm
value = "0 7 0 0 0 0 0 9 1, " \
        "0 5 0 3 0 0 0 2 0, " \
        "0 0 0 8 0 0 0 4 5, " \
        "0 8 5 0 3 0 0 0 0, " \
        "0 3 0 0 0 8 0 6 2, " \
        "0 1 9 0 6 0 0 0 0, " \
        "0 0 0 4 0 0 0 0 0, " \
        "0 4 2 0 1 5 0 8 7, " \
        "0 0 0 6 0 3 2 5 0"

board = [list(map(int, each.strip().split())) for each in value.split(',')]


def style(arr):
    temp = ''
    for i in range(len(arr)):
        if (i + 1) % 3 == 0 and i + 1 != 9:
            temp += str(arr[i])+' | '
        else:
            temp += str(arr[i])+' '

    return temp


def print_board(board):
    for i in range(len(board)):
        if i == 9:
            break
        if (i + 1) % 3 == 0 and i + 1 != 9:
            print(style(board[i])+'\n'+'- - - - - - - - - - -')
        else:
            print(style(board[i]))


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j   # position
    return None


def valid(board, num, pos):
    # check validity along row
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check validity along column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check Validity Inside the Square
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(board, num, (row,col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0

    return False


print_board(board)
solve(board)
print('---------------------')
print_board(board)


