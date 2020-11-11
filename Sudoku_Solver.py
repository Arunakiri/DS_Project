# Solving Sudoku using Backtracking(Recursive) Algorithm
def solve(board):
    # print(board)  # Shows what happens each step
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


# Check for validity of the number on a position in the board
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


# Adding Formats
def style(arr):
    temp = ''
    for i in range(len(arr)):
        if (i + 1) % 3 == 0 and i + 1 != 9:
            temp += str(arr[i])+' | '
        else:
            temp += str(arr[i])+' '

    return temp


# Print the Board
def print_board(board):
    for i in range(len(board)):
        if i == 9:
            break
        if (i + 1) % 3 == 0 and i + 1 != 9:
            print(style(board[i])+'\n'+'- - - - - - - - - - -')
        else:
            print(style(board[i]))


# Find the empty position on the board
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j   # position
    return None


value = "7 8 0 4 0 0 1 2 0, " \
        "6 0 0 0 7 5 0 0 9, " \
        "0 0 0 6 0 1 0 7 8, " \
        "0 0 7 0 4 0 2 6 0, " \
        "0 0 1 0 5 0 9 3 0, " \
        "9 0 4 0 6 0 0 0 5, " \
        "0 7 0 3 0 0 0 1 2, " \
        "1 2 0 0 0 7 4 0 0, " \
        "0 4 9 2 0 6 0 0 7"

board = [list(map(int, each.strip().split())) for each in value.split(',')]

# print_board(board)
solve(board)
# print('---------------------')
print_board(board)


