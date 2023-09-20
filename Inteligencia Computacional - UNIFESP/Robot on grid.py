grid = {}
MOD = 2**31-1

def matrix(grid):
    n = len(grid)
    df = [[0]* n for _ in range(n)]
    df[0][0] = 1

    for i in range(1,n):
        if grid[i][0] == '.':
            df[i][0] == df[i-1][0]

    for j in range(1,n):
        if grid[0][j] == '.':
            df[0][j] = df[0][j-1]
    
    for i in range(1,n):
        for j in range(1, n):
            if grid[i][j] == '.':
                df[i][j] = (df[i - 1][j] + df[i][j - 1] % MOD)
    
    return df[n - 1][n - 1]

n = int(input())
grid = [input() for i in range(n)]

result = matrix(grid)

if result == 0:
    up_left = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "#" and (i>0 and grid[i-1][j] == '.') and (j > 0 and grid[i][j - 1] == '.'):
                up_left = True
                break

    if up_left == True:
        print("THE GAME IS A LIE")

    else:
        print("INCONCEIVABLE")
else:
    print(result)