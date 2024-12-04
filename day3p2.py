from re import findall

total = 0
enabled = True
data = open('day3.txt').read()

for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do:
        enabled = True
    elif dont:
        enabled = False
    else:
        x = int(a) * int(b)
        if(enabled):
            total += x

print(total)