day = "03"
inp = open("input/{}.txt".format(day)).read()

round = 0
priority_sum = 0
sec = set()


for line in inp.split("\n")[:-1]:
    l = len(line)
    if round == 0:
        sec = set(c for c in line)
    else:
        sec = sec.intersection(set(c for c in line))

    if round == 2:
        overlapping = next(iter(sec))
        prio = 0

        if overlapping.lower() == overlapping:
            prio = ord(overlapping) - ord("a") + 1
        else:
            prio = ord(overlapping) - ord("A") + 27

        priority_sum += prio
        round = 0
        sec = set()
    else:
        round += 1

print(priority_sum)
