day = "04"
inp = open("input/{}.txt".format(day)).read()

res = 0

for line in inp.splitlines():
    a, b = line.split(",")
    aa, ab = list(map(int, a.split("-")))
    ba, bb = list(map(int, b.split("-")))

    if aa <= ba <= bb <= ab or ba <= aa <= ab <= bb:
        res += 1

print(res)
