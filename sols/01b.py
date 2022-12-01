day = "01"
inp = open("input/{}.txt".format(day)).read()

nums = []
b = inp.split("\n\n")
for i in b:
    nums.append(sum(list(map(int, i.split()))))

nums.sort(reverse=True)
print(sum(nums[0:3]))
