#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(n):
    if n < 4:
        return []
    
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(board, col):
        if col >= n:
            solution = []
            for row in board:
                queen_col = row.index(1)
                solution.append([queen_col, row.index(queen_col)])
            solutions.append(solution)
            return True
        
        res = False
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                res = solve(board, col + 1) or res
                board[i][col] = 0
        
        return res

    if solve(board, 0):
        return solutions
    else:
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
