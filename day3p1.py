from re import findall

total = 0
enabled = True
data = open('day3.txt').read()

for a, b in findall(r"mul\((\d+),(\d+)\)", data):
    total += int(a) * int(b)

print(total)