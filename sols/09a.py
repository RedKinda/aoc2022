day = "09"
inp = open("input/{}.txt".format(day)).read()

visited = set()

head_x = 0
head_y = 0
tail_x = 0
tail_y = 0


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

        xdiff = head_x - tail_x
        ydiff = head_y - tail_y

        if abs(xdiff) > 1 or (abs(ydiff) > 1 and abs(xdiff) > 0):
            if tail_x < head_x:
                tail_x += 1
            else:
                tail_x -= 1

        if abs(ydiff) > 1 or (abs(xdiff) > 1 and abs(ydiff) > 0):
            if tail_y < head_y:
                tail_y += 1
            else:
                tail_y -= 1

        visited.add((tail_x, tail_y))

print(len(visited))
