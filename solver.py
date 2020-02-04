import time

BOARD_SIZE = 8  # it is advised not to use a board size bigger than 20
QUEEN_TOKEN = 'Q'  # the representation of the queen on the board structure


def is_queen_safe(board, row, col):
    '''Checks if a queen can be safely placed in the square specified by (row, col)'''
    return is_queen_safe_row(board, row) and is_queen_safe_col(board, col) and is_queen_safe_diagonals(board, row, col)


def is_queen_safe_row(board, row):
    '''Checks if a queen can be safely placed in the specified row'''
    for y in range(BOARD_SIZE):
        if board[row][y] == QUEEN_TOKEN:
            return False
    return True


def is_queen_safe_col(board, col):
    '''Checks if a queen can be safely placed in the specified column'''
    for x in range(BOARD_SIZE):
        if board[x][col] == QUEEN_TOKEN:
            return False
    return True


def is_queen_safe_diagonals(board, row, col):
    '''Checks if a queen can be safely placed in the diagonals crossing through the square specified by (row, col)'''
    for offset in range(1, row + 1):
        if row - offset >= 0 and col + offset < BOARD_SIZE:
            if board[row - offset][col + offset] == QUEEN_TOKEN:
                return False
        if col - offset >= 0 and col - offset >= 0:
            if board[row - offset][col - offset] == QUEEN_TOKEN:
                return False
    return True


def generate_empty_board():
    '''Generate and empty chessboard

    Returns:
        list[list[int]]: A 2D list of all-zeros that represents an empty chessboard
    '''
    board = []

    for i in range(BOARD_SIZE):
        board.append([])
        for _ in range(BOARD_SIZE):
            board[i].append(0)
    return board


def print_board(board):
    '''Print the chessboard'''
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(board[i][j], end=' ')
        print()
    print()


def solve(board, curr_row=0):
    '''Recursively solves and prints all solutions to the N-Queens Problem
    
    Args:
        board (list[list[int]]): The board structure on which the problem will be solved
        curr_row (int): The index of the row where a queen could be placed
    '''
    if curr_row == BOARD_SIZE:
        print_board(board)
    else:
        for col in range(BOARD_SIZE):
            if is_queen_safe(board, curr_row, col):
                board[curr_row][col] = QUEEN_TOKEN
                solve(board, curr_row + 1)
                board[curr_row][col] = 0


if __name__ == '__main__':
    board = generate_empty_board()
    t1 = time.perf_counter()
    solve(board)
    t2 = time.perf_counter()
    print(f'Time taken: {t2 - t1}s')
