day = "09"
inp = open("input/{}.txt".format(day)).read()

visited = set()

head_x = 0
head_y = 0

nparts = 10
parts = [(0, 0) for i in range(nparts)]


for line in inp.splitlines():
    dir, amount = line[0], int(line[1:])
    for i in range(amount):
        if dir == "U":
            head_y += 1
        elif dir == "D":
            head_y -= 1
        elif dir == "L":
            head_x -= 1
        elif dir == "R":
            head_x += 1

        parts[0] = (head_x, head_y)

        for i in range(1, nparts):
            tail_x = parts[i][0]
            tail_y = parts[i][1]
            xdiff = parts[i - 1][0] - tail_x
            ydiff = parts[i - 1][1] - tail_y

            if abs(xdiff) > 1 or (abs(ydiff) > 1 and abs(xdiff) > 0):
                if tail_x < parts[i - 1][0]:
                    tail_x += 1
                else:
                    tail_x -= 1

            if abs(ydiff) > 1 or (abs(xdiff) > 1 and abs(ydiff) > 0):
                if tail_y < parts[i - 1][1]:
                    tail_y += 1
                else:
                    tail_y -= 1

            parts[i] = (tail_x, tail_y)

        visited.add(parts[-1])

print(len(visited))
