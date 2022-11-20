#2-dimensional lists

number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

#accessing elements in the 2d list... the values in the square brackets are the rows and columns
print(number_grid[1][0])

for row in number_grid:
    for column in row:
        print(column)