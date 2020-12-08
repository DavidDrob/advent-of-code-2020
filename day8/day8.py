input = open('day8input.txt', 'r')
lines = input.readlines()

accumulator = 0
idx = 0
alreadyRan = []

while True:
    if idx in alreadyRan:
        print(accumulator)
        break
    if lines[idx][0:3] == 'nop':
        alreadyRan.append(idx)
        idx += 1
    elif lines[idx][0:3] == 'acc':
        alreadyRan.append(idx)
        accumulator += int(lines[idx][4:])
        idx += 1
    else:
        alreadyRan.append(idx)
        jump = lines[idx][4:]
        idx += int(jump)
