size = 6

tbl = []
for i in range(size):
        temp = [1]
        for j in range(size-1):
                temp.append(0)
        tbl.append(temp) 

for row in range(1,size):
        for col in range(1,row + 1):
                tbl[row][col] = tbl[row-1][col] + tbl[row][col-1]
print(tbl)                