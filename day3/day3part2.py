input = open('day3input.txt', 'r')
line = input.readlines()

meX = 0
meY = 0
treesEnc = 0
treesSum = 0
idx = 0
solution = []
result = 1
meXArray = [1,3,5,7,1]
meYArray = [1,1,1,1,2]

def main(line, meX, meY, treesEnc, meXArray, meYArray, idx):
    while meY < 323:
        pos = line[meY].replace("\n", "")
        pos = pos *89
        if '#' in pos[meX]:
            treesEnc += 1
        meX += meXArray[idx]
        meY += meYArray[idx]
    return treesEnc


while idx < 5:
    solution.append(main(line, meX, meY, treesEnc, meXArray, meYArray, idx))
    idx += 1

for i in solution:
    result = result * i

print(result)


input.close()