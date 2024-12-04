with open('day4.txt', 'r') as file:
    data = [list(line.strip()) for line in file]

res = 0
dirs = [(1, 1), (1, -1)]

def searchfroma(row, col):
    count = 0
    if row < len(data)-1 and row > 0 and col < len(data[0])-1 and col > 0:
        x, y = dirs[0]
        if (data[row+x][col+y] == 'M' and data[row+x*-1][col+y*-1] == 'S' or data[row+x][col+y] == 'S' and data[row+x*-1][col+y*-1] == 'M'):
            x, y = dirs[1]
            if (data[row+x][col+y] == 'M' and data[row+x*-1][col+y*-1] == 'S' or data[row+x][col+y] == 'S' and data[row+x*-1][col+y*-1] == 'M'):
                count += 1
    return count
    
for i in range(len(data)):
    for j in range(len(data[0])):
        if (data[i][j] == 'A'):
            res += searchfroma(i, j)
 
print(res)

