with open('day1.txt', 'r') as file:
    firsts = []
    seconds = []
    
    for line in file:
        first, second = map(int, line.split())
        firsts.append(first)
        seconds.append(second)

firsts.sort()
seconds.sort()

res = 0

for i in range(len(firsts)):
    res += abs(firsts[i] - seconds[i])

print(res)
    