with open('day4.txt', 'r') as file:
    data = [list(line.strip()) for line in file]

res = 0
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def searchfromx(row, col):
    count = 0
    for x, y in dirs:
        if row+x*3 < len(data) and row+x*3 >= 0 and col+y*3 < len(data[0]) and col+y*3 >= 0:
            if (data[row+x][col+y] == 'M' and data[row+x*2][col+y*2] == 'A' and data[row+x*3][col+y*3] == 'S'):
                count += 1
    return count
    
for i in range(len(data)):
    for j in range(len(data[0])):
        if (data[i][j] == 'X'):
            res += searchfromx(i, j)
 
print(res)

