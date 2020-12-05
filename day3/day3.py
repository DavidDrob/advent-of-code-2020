input = open('day3input.txt', 'r')
line = input.readlines()

meX = 0
meY = 0
treesEnc = 0
treesSum = 0
idx = 0
solution = []
result = 1

def main(line, meX, meY, treesEnc):
    while meY < 323:
        pos = line[meY].replace("\n", "")
        pos = pos *89
        if '#' in pos[meX]:
            treesEnc += 1
        meX += 3
        meY += 1
    print(treesEnc) 

main(line, meX, meY, treesEnc)