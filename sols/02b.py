day = "02"
inp = open("input/{}.txt".format(day)).read()

score = 0
# X is lose, Y is draw, and Z is win.
s = {"A": 1, "B": 2, "C": 3}


for row in inp[:-1].split("\n"):
    a, b = row.split()

    if b == "Z":
        toadd = 6 + (s[a]) % 3 + 1
    elif b == "Y":
        toadd = 3 + s[a]
    elif b == "X":
        toadd = ((s[a] - 2) % 3) + 1
    else:
        raise Exception("Invalid input")

    score += toadd


print(score)
