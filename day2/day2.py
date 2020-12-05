input = open('day2input.txt', 'r+')
line = input.readlines()

fromTo = 0
letter = 1
password = 2

idx = 0
validPWs = 0

def everything(line, idx, validPWs):
    for i in range(1000):
        letterArray = line[idx].split()[letter]
        letterArray = letterArray.replace(":", "")

        passwordArray = line[idx].split()[password]

        fromToArray = line[idx].split()[fromTo]
        fromToArray = fromToArray.replace("-", " ")
        fromToArray = fromToArray.split()

        if letterArray in passwordArray:
            if passwordArray.count(letterArray) in range(int(fromToArray[0]), int(fromToArray[1])+1): # +1 because it should only be true if the number is smaller or EQUAL to the maximum
                validPWs += 1
        idx += 1
    print("There are {} valid passwords".format(validPWs))


everything(line, idx, validPWs)
input.close()