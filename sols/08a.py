day = "08"
inp = open("input/{}.txt".format(day)).read()

res = set()

grid = [[int(c) for c in line] for line in inp.splitlines()]
width = len(grid[0])
height = len(grid)

for i in range(height):
    lowestnum = -1
    for j in range(width):
        if grid[i][j] > lowestnum:
            lowestnum = grid[i][j]
            res.add((i, j))

for i in range(height):
    lowestnum = -1
    for j in range(width):
        if grid[i][width - j - 1] > lowestnum:
            lowestnum = grid[i][width - j - 1]
            res.add((i, width - j - 1))

for i in range(width):
    lowestnum = -1
    for j in range(height):
        if grid[j][i] > lowestnum:
            lowestnum = grid[j][i]
            res.add((j, i))

for i in range(width):
    lowestnum = -1
    for j in range(height):
        if grid[height - j - 1][i] > lowestnum:
            lowestnum = grid[height - j - 1][i]
            res.add((height - j - 1, i))

print(len(res))
