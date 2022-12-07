day = "06"
inp = open("input/{}.txt".format(day)).read()

for i in range(0, len(inp) - 14):
    chars = set(inp[i : i + 14])
    if len(chars) == 14:
        print("".join(chars))
        print(i + 14)
        break
