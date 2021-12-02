
input0 = []
with open("demo.dat") as f:
    for line in f:
        line = line.rstrip('\n')
        input0.append(line)

print(input0)
print(input0[0].split())

class Submarine:
    def __init__(self):
        self.x = 0
        self.y = 0

    def dive(self, dir, amount):
        if "forward" in dir:
            self.x += amount
        elif "down" in dir:
            self.y += amount
        elif "up" in dir:
            self.y -= amount


    def __str__(self):
        return f"We are at x = {self.x} & y = {self.y}\n\
            Product = {self.x * self.y}"
        
yellowSubmarine = Submarine()
for data in input0:
    d2 = data.split()
    yellowSubmarine.dive(d2[0], int(d2[1]))

print(yellowSubmarine)
