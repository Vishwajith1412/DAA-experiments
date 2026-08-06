def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]
        if placed == col:  # Same column
            return False
        if abs(prev_row - row) == abs(placed - col):  # Diagonal check
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Undo placement
            backtrack_count[0] += 1

    backtrack(0)
    return solutions, backtrack_count[0]

def display_board(solution, n):
    print(' +' + '---+' * n)
    for row in range(n):
        print(' |', end='')
        for col in range(n):
            if solution[row] == col:
                print(' Q |', end='')
            else:
                print(' . |', end='')
        print()
        print(' +' + '---+' * n)

# --- Solve for N=5 (showing only first 2 solutions) and N=7, N=9 (count only) ---
for n in [5, 7, 9]:
    solutions, backtracks = solve_n_queens(n)
    print(f'\nN={n}: {len(solutions)} solutions, {backtracks} backtracks')
    
    if n == 5:
        max_display = 2  # Modified: Limit visual display to first 2 solutions only
        print(f'\nFirst {max_display} solutions for {n}-Queens:')
        for i in range(max_display):
            sol = solutions[i]
            print(f'\nSolution {i+1}: {sol}')
            display_board(sol, n)
