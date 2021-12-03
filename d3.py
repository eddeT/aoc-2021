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
result.prepend("0b000")
resultInv.invert()
resultInv.prepend("0b000")


print (resultInv.int * result.int)