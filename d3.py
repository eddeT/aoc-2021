from array import array
from operator import eq, pos
from bitstring import BitArray, BitStream, BitString

def readData(filename):
    with open(filename) as f:
        input = []
        for line in f:
            line = line.rstrip('\n')
            a = BitArray(f"0b{line}")
            input.append(a)
        return input

data = readData("d3.dat")

rows = []

for j, b in enumerate(data):
    for i in range(0,len(b)):
        if j == 0:
            rows.append(b[i:i+1])
        else:
            rows[i].append(b[i:i+1])

result= BitArray()

for r in rows:
    if r.count(1) > r.count(0):
        result.append("0b1")
    else:
        result.append("0b0")



resultInv = result.copy()
result.prepend("0b0000")
resultInv.invert()
resultInv.prepend("0b0000")

print (result.bin)
print (resultInv.bin)
print (resultInv.int * result.int)

toUse = list(range(0, len(data)))
resArrayP = []
for i in range (0, len(data[0])):
    pos = 0
    neg = 0
    posArray = []
    negArray = []
    for j in toUse:
        if data[j][i]:
            pos += 1
            posArray.append(j)
        else:
            neg += 1
            negArray.append(j)
    if pos >= neg:
        resArrayP.append(posArray)
    else:
        resArrayP.append(negArray)
    toUse = resArrayP[i]
    if len(toUse) == 1:
        break

o2= data[resArrayP[-1][-1]]
o2.prepend("0b0000")

print (o2.int)


toUse = list(range(0, len(data)))
resArrayN = []
for i in range (0, len(data[0])):
    pos = 0
    neg = 0
    posArray = []
    negArray = []
    for j in toUse:
        if data[j][i]:
            pos += 1
            posArray.append(j)
        else:
            neg += 1
            negArray.append(j)
    if pos >= neg:
        resArrayN.append(negArray)
    else:
        resArrayN.append(posArray)
    toUse = resArrayN[i]
    if len(toUse) == 1:
        break

print(resArrayN)
co2= data[resArrayN[-1][-1]]
co2.prepend("0b0000")

print (co2.int)

print (co2.int*o2.int)

