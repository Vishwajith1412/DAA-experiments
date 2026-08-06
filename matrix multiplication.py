def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming
    dims: list of dimensions where matrix A_i has dimensions dims[i-1] x dims[i]
    Time Complexity: O(n^3), Space Complexity: O(n^2)
    """
    n = len(dims) - 1
    # m[i][j] = minimum multiplications for matrices i..j
    m = [[0] * (n + 1) for _ in range(n + 1)]
    # s[i][j] = index k that achieves optimal split
    s = [[0] * (n + 1) for _ in range(n + 1)]
    
    # l is the chain length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + dims[i-1] * dims[k] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k  # Fixed: correctly placed inside the if statement
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        return f'A{i}'
    k = s[i][j]
    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)
    return f'({left} x {right})'

def print_dp_table(m, n):
    print('\nDP Cost Table m[i][j]:')
    print(f'{"":>6}', end='')
    for j in range(1, n + 1):
        print(f'A{j:>8}', end='')
    print()
    for i in range(1, n + 1):
        print(f'A{i:<5}', end='')
        for j in range(1, n + 1):
            if j < i: 
                print(f'{"---":>9}', end='')
            else: 
                print(f'{m[i][j]:>9}', end='')
        print()

# --- Updated Input Dimensions ---
# Matrices: A1(5x10), A2(10x20), A3(20x10), A4(10x30), A5(30x8)
dims = [5, 10, 20, 10, 30, 8]
n = len(dims) - 1

print('Matrix Dimensions:')
for i in range(n):
    print(f' A{i+1}: {dims[i]} x {dims[i+1]}')

m, s = matrix_chain_order(dims)

print(f'\nMinimum scalar multiplications: {m[1][n]}')
print(f'Optimal parenthesization: {print_optimal_parens(s, 1, n)}')
print_dp_table(m, n)
