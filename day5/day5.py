input = open('day5input.txt', 'r')
line = input.readlines()

row = []
col = []
rb = ''
cb = ''
idx = 0
seats = []

def rowBin(rb, idx, row, cb, col, seats):
    rowIDX = line[idx][:7]
    for i in rowIDX:
        if i == 'B':
            i = 1
        else:
            i = 0
        row.append(i)
    for j in range(7):
        rb += str(row[j])
    rb = int(rb, 2)
    colIDX = line[idx][7:10]
    for a in colIDX:
        if a == 'R':
            a = 1
        else:
            a = 0
        col.append(a)
    for b in range(3):
        cb += str(col[b])
    cb = int(cb, 2)
    seats.append(rb*8+cb)

for x in range(len(line)):
    rowBin(rb, idx, row, cb, col, seats)
    idx += 1
    row = []
    col = []

print("The highest seat ID is {0}".format(max(seats)))
   
for seat in seats:
    if seat+1 not in seats and seat-1 in seats:
        print("My seat is :{0}".format(seat))
