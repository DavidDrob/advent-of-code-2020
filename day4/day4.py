# Doesn't work

input = open('day4input.txt', 'r')
lines = input.readlines()

lines = [line.strip() for line in lines]
passport = ''

requirements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
ans = 0

for line in lines:
    passport = line
    passport.split(" ")
    if line != '':
        passport.split()
        passport.split(":")
        print(passport)
        for i in passport:
            key, value = passport.split(":")
        print(passport)
        for requirement in requirements:
            if requirement in passport:
                ans += 1
    passport = ''
print(ans)

input.close()