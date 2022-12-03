day = "02"
inp = open("input/{}.txt".format(day)).read()

score = 0
# X is rock, Y is paper, and Z is scissors.
s = {"X": 1, "Y": 2, "Z": 3}


for row in inp.split("\n"):
    a, b = row.split()
    score_now = 0
    # A B C is rock, paper, scissors
    if a == "A":
        if b == "Y":
            score_now = 6
        elif b == "X":
            score_now = 3
        elif b == "Z":
            score_now = 0
    elif a == "B":
        if b == "X":
            score_now = 0
        elif b == "Y":
            score_now = 3
        elif b == "Z":
            score_now = 6
    elif a == "C":
        if b == "Z":
            score_now = 3
        elif b == "Y":
            score_now = 0
        elif b == "X":
            score_now = 6

    toadd = s[b] + score_now
    score += toadd

print(score)