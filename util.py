

def readLinesToList(pth):
    res = []
    with open(pth, 'r') as file:
        for line in file:
            res.append(line.strip())
    return res
