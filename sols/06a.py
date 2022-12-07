day = "06"
inp = open("input/{}.txt".format(day)).read()

for i in range(0, len(inp) - 4):
    chars = set(inp[i : i + 4])
    if len(chars) == 4:
        print("".join(chars))
        print(i + 4)
        break
