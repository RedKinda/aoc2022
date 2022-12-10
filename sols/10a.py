day = "10"
inp = open("input/{}.txt".format(day)).read()

x = 1

cycle = 0

qs = {20: None, 60: None, 100: None, 140: None, 180: None, 220: None}

for line in inp.splitlines():
    words = line.split()
    toadd = 0

    if words[0] == "noop":
        cycle += 1

    elif words[0] == "addx":
        cycle += 2
        toadd = int(words[1])

    for q, val in qs.items():
        if cycle >= q and val is None:
            qs[q] = x * q

    x += toadd

print(sum(qs.values()))
