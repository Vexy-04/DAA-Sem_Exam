def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 'Q':
            return False
    return True

def solve_n_queens(n):
    solutions = []

    def backtrack(row, board):
        if row == n:
            solutions.append([' '.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(row + 1, board)
                board[row][col] = '*'

    backtrack(0, [['*' for _ in range(n)] for _ in range(n)])
    return solutions

def print_solutions(solutions):
    if solutions:
        for sol in solutions:
            for row in sol:
                print(row)
            print()
    else:
        print("Not Possible!")

N = int(input("Enter the number of Queens: "))
print_solutions(solve_n_queens(N))

'''
Enter the number of Queens: 4
* Q * *
* * * Q
Q * * *
* * Q *

* * Q *
Q * * *
* * * Q
* Q * *
'''