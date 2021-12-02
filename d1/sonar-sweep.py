input1 = []

with open("sonar-sweep.dat") as f:
    for line in f:
        line = line.rstrip('\n')
        input1.append(int(line))



input2 = []
for i, val in enumerate(input1):
    if i < len(input1)-2:
        input2.append(val+input1[i+1]+input1[i+2])
        #print(newInput[-1])


def findDepth(input):
    largerCount = 0
    for i, val in enumerate(input):
        #print(f"{val} {i}")
        if i > 0:
            if val > input[i-1]:
                largerCount += 1

    return (f"Final depth count: {largerCount}")


print(f"First mission: {findDepth(input1)}")

print(f"Second mission: {findDepth(input2)}")
