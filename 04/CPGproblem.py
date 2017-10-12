#character picture graph problem
grid =  [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]
'''
I copied this code. I cant think of a solution that is not tedious.
'''
'''
for j in range(len(grid[0])):
    for i in range(0, len(grid)):
        print(grid[i][j], end='')
    print()

#a=[[1,2],[3,4],[5,6]]
print(grid[0][0], [1][0], [2][0], [3][0], [4][0], end='')
print(grid[1][0])
'''
'''
print(grid[0][0],end='')
print(grid[1][0],end='')
print(grid[2][0],end='')
print(grid[3][0],end='')
print(grid[4][0],end='')
print(grid[5][0],end='')
print(grid[6][0],end='')
print(grid[7][0],end='')
print(grid[8][0])

print(grid[0][1],end='')
print(grid[1][1],end='')
print(grid[2][1],end='')
print(grid[3][1],end='')
print(grid[4][1],end='')
print(grid[5][1],end='')
print(grid[6][1],end='')
print(grid[7][1],end='')
print(grid[8][1])

print(grid[0][2],end='')
print(grid[1][2],end='')
print(grid[2][2],end='')
print(grid[3][2],end='')
print(grid[4][2],end='')
print(grid[5][2],end='')
print(grid[6][2],end='')
print(grid[7][2],end='')
print(grid[8][2])

print(grid[0][3],end='')
print(grid[1][3],end='')
print(grid[2][3],end='')
print(grid[3][3],end='')
print(grid[4][3],end='')
print(grid[5][3],end='')
print(grid[6][3],end='')
print(grid[7][3],end='')
print(grid[8][3])

print(grid[0][4],end='')
print(grid[1][4],end='')
print(grid[2][4],end='')
print(grid[3][4],end='')
print(grid[4][4],end='')
print(grid[5][4],end='')
print(grid[6][4],end='')
print(grid[7][4],end='')
print(grid[8][4])

print(grid[0][5],end='')
print(grid[1][5],end='')
print(grid[2][5],end='')
print(grid[3][5],end='')
print(grid[4][5],end='')
print(grid[5][5],end='')
print(grid[6][5],end='')
print(grid[7][5],end='')
print(grid[8][5])

print(grid[0][0],grid[1][0],grid[2][0],grid[3][0],grid[4][0],grid[5][0],grid[6][0],grid[7][0],grid[8][0])
print(grid[0][1],grid[1][1],grid[2][1],grid[3][1],grid[4][1],grid[5][1],grid[6][1],grid[7][1],grid[8][1])
for i in range(len(grid[0:-1][0])):
    print (str(chr(i)))
#How do i print the .s and 0s in the [x][0] place with for i in range and print?
'''
print(grid[0][0],grid[1][0],grid[2][0],grid[3][0],grid[4][0],grid[5][0],grid[6][0],grid[7][0],grid[8][0])
