day = "03"
inp = open("input/{}.txt".format(day)).read()

priority_sum = 0
for line in inp.split("\n")[:-1]:
    l = len(line)
    a, b = line[0 : l // 2], line[l // 2 :]

    sa = set(c for c in a)
    sb = set(c for c in b)

    intersection = sa.intersection(sb)
    overlapping = next(iter(intersection))

    prio = 0

    if overlapping.lower() == overlapping:
        prio = ord(overlapping) - ord("a") + 1
    else:
        prio = ord(overlapping) - ord("A") + 27

    priority_sum += prio

print(priority_sum)
