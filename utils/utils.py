def readData(filename):
    with open(filename) as f:
        input = []
        for line in f:
            line = line.rstrip('\n')
            input.append(int(line))
        return input