idx = 0
answers = []
uniqueAnswers = []
x = 0
suma = 0

input = open("day6input.txt").read().split("\n\n")

for i in range(454):
    currentLine = list(input[idx].replace('\n', ''))
    for answer in currentLine:
        if answer not in answers:
            answers.append(answer)
            uniqueAnswers.append(len(answers))
    newUniqueAnswers = max(uniqueAnswers)
    suma += newUniqueAnswers
    idx += 1
    answers = []
    uniqueAnswers = []
print("{0} people answered yes".format(suma))