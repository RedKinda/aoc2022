day = "10"
inp = open("input/{}.txt".format(day)).read()

x = 1

cycle = 0

drawing = []


def draw(cycle, x):
    if abs((cycle % 40) - x) <= 1:
        drawing.append("#")
    else:
        drawing.append(".")


for line in inp.splitlines():
    words = line.split()
    toadd = 0
    draw(cycle, x)

    if words[0] == "noop":
        cycle += 1

    elif words[0] == "addx":
        draw(cycle + 1, x)
        cycle += 2
        toadd = int(words[1])

    x += toadd

for i in range(6):
    print("".join(drawing[i * 40 : (i + 1) * 40]))
