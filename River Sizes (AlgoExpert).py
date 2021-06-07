# Description: You are given a two-dimensional array (matrix)
# of potentially unequal height and width containing only 0s and 1s.
# Each 0 represents land, and each 1 represents part of a river.
# A river consists of any number of 1s that are either horizontally or vertically
# adjacent (but not diagonally adjacent). The number of adjacent 1s forming a river determine its size.
# Write a function that returns an array of the sizes of all rivers represented in the input matrix.
# Note that these sizes do not need to be in any particular order.

#Sample input:
#[
#    [1, 0, 0, 1, 0],
#    [1, 0, 1, 0, 0],
#    [0, 0, 1, 0, 1],
#    [1, 0, 1, 0, 1],
#    [1, 0, 1, 1, 0],
#]
#Sample output:
#   [1, 2, 2, 2, 5]

def riversize(matrix):
    marked = set() #coordinates marked with '1'
    rivers = [] #output list with river lengths
    for row in range(len(matrix)):
        # look for every single position:
        for column in range(len(matrix[row])):
            el = matrix[row][column] # current element (1 or 0)
            coordinates = (row, column) # coordinates of the current element
            if el == 1 and coordinates not in marked:
                marked.add(coordinates)
                current_river_length = 1
                stack = [coordinates] #coordinates of the 1s in a current river

                while stack:
                    current = stack.pop() #takes the last 1-coordinates to look for their neighbours
                    neighbours = get_neighbours(current, matrix) #gets all the neighbors of the last coordinates
                    for n in neighbours:
                        x, y = n
                        if matrix[x][y] == 1 and (x, y) not in marked: #is in the matrix but not yet marked
                            marked.add((x, y))
                            current_river_length += 1
                            stack.append((x, y)) #appends the freshest coordinates to the stack to check its neighbours

            rivers.append(current_river_length)
    return rivers



def get_neighbours(xyposition, matrix): #looks for the position of the left, right, upper, downer neighbour
    x, y = xyposition #x == rows, y == columns
    neighbors = []
    if x >= 1: #left neighbour
        neighbors.append((x - 1, y))
    if x < (len(matrix) - 1):
        neighbors.append((x + 1, y))
    if y >= 1: #left neighbour
        neighbors.append((x, y - 1))
    if y < (len(matrix[0]) - 1):
        neighbors.append((x, y + 1))

    return neighbors
