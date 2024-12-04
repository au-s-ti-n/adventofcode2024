with open('day1.txt', 'r') as file:
    firsts = []
    seconds = []
    
    for line in file:
        first, second = map(int, line.split())
        firsts.append(first)
        seconds.append(second)

res = 0

for i in range(len(firsts)):
    matches = 0
    for j in range(len(seconds)):
        if (firsts[i] == seconds[j]):
            matches += 1
    res += firsts[i] * matches

print(res)
    