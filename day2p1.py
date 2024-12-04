def safe(row):
    if (row[0] == row[1]):
        return False
    elif (row[0] > row[1] and row[0] - row[1] <= 3): #decreasing
        for i in range(1, len(row)-1):
            if not (row[i] > row[i+1] and row[i] - row[i+1] <= 3):
                return False
        return True
    elif (row[0] < row[1] and row[1] - row[0] <= 3): #increasing
        for i in range(1, len(row)-1):
            if not (row[i] < row[i+1] and row[i+1] - row[i] <= 3):
                return False
        return True

with open('day2.txt', 'r') as f:
    data = f.read().strip().split('\n')

res = 0

for d in data:
    row = list(map(int, d.split()))
    if safe(row):
        res += 1

print(res)
