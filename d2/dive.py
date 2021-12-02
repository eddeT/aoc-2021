
input0 = []
with open("dive.dat") as f:
    for line in f:
        line = line.rstrip('\n')
        input0.append(line)

class SubmarineAlfa:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def dive(self, dir, amount):
        if "forward" in dir:
            self.horizontal += amount
        elif "down" in dir:
            self.depth += amount
        elif "up" in dir:
            self.depth -= amount


    def __str__(self):
        return f"Horizontal = {self.horizontal} Depth = {self.depth}\n\
            Product = {self.horizontal * self.depth}"

class SubmarineBeta:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def dive(self, dir, amount):
        if "forward" in dir:
            self.horizontal += amount
            self.depth += self.aim * amount
        elif "down" in dir:
            self.aim += amount
        elif "up" in dir:
            self.aim -= amount


    def __str__(self):
        return f"Horizontal = {self.horizontal} Depth = {self.depth} Aim = {self.aim}\n\
            Product = {self.horizontal * self.depth}"
        
yellowSubmarine = SubmarineBeta()
for data in input0:
    d2 = data.split()
    yellowSubmarine.dive(d2[0], int(d2[1]))

print(yellowSubmarine)
