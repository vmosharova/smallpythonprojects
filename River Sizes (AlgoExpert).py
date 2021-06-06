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
    riverlength = [] #output list with river lengths
    for row in range(len(matrix)):
        for column in range(len(row)):
            el = matrix[row][column] # current element (1 or 0)
            coordinates = (row, column) # coordinates of the current element
            if el == 1 and coordinates not in marked:
                marked.add(coordinates)



