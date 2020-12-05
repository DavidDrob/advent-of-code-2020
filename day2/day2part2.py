input = open('day2input.txt', 'r+')
line = input.readlines()

idx = 0
validPWs = 0

def everything(line, idx, validPWs):
    for i in range(1000):
        letter = line[idx].split()[1]
        letter = letter.replace(":", "")

        password = list(line[idx].split()[2])

        fromTo = line[idx].split()[0]
        fromTo = fromTo.replace("-", " ")
        fromTo = fromTo.split()

        #Toboggan Corporate Policies have no concept of "index zero"! That's the reason why I put '-1' for the index
        if bool(letter in password[int(fromTo[1])-1]) ^ bool(letter in password[int(fromTo[0])-1]):
            validPWs += 1

        idx += 1
    print("There are {0} valid passwords".format(validPWs))

everything(line, idx, validPWs)
input.close()