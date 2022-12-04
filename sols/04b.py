day = "04"
inp = open("input/{}.txt".format(day)).read()

res = 0

for line in inp.splitlines():
    a, b = line.split(",")
    aa, ab = list(map(int, a.split("-")))
    ba, bb = list(map(int, b.split("-")))

    if (ba <= ab and aa <= bb) or (aa <= bb and ba <= ab):
        res += 1

print(res)
