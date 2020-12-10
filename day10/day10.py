input = open('day10input.txt', 'r')
lines = input.readlines()

def mainF(outlet,  diff1, diff3):
    if outlet + 1 in [int(line.strip()) for line in lines]:
        outlet += 1
        diff1 += 1
        mainF(outlet, diff1, diff3)
    elif outlet + 2 in [int(line.strip()) for line in lines]:
        outlet += 2
        mainF(outlet, diff1, diff3)
    elif outlet + 3 in [int(line.strip()) for line in lines]:
        outlet += 3
        diff3 += 1
        mainF(outlet, diff1, diff3)
    else:
        print('difference =',diff1*(diff3+1)) # +1 because the first time you have to do the first one manually 
    
mainF(0, 0, 0)

input.close()