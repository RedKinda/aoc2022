day = "07"
inp = open("input/{}.txt".format(day)).read()


class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.files = []

    @property
    def size(self):
        return sum(f.size for f in self.files)

    def visit_all(self, res, limit=100000):
        if self.size < limit:
            res.append(self)
        for f in self.files:
            if isinstance(f, Dir):
                f.visit_all(res, limit)


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


root = Dir("root", None)
current_dir: Dir = root

for line in inp.splitlines():
    words = line.split()
    if words[0] == "$":
        if words[1] == "cd":
            if words[2] == "..":
                current_dir = current_dir.parent
            else:
                for f in current_dir.files:
                    if f.name == words[2]:
                        current_dir = f
                        break

        elif words[1] == "ls":
            continue

    else:
        size, name = words
        if size == "dir":
            current_dir.files.append(Dir(name, current_dir))
        else:
            current_dir.files.append(File(name, int(size)))


# Find all dirs with size less than 100000
dirs = []
root.visit_all(dirs, 100000)

# print sum of sizes
print(sum(d.size for d in dirs))
