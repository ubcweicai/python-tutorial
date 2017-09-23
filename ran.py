# so i'd like to use the same into my code, but got error message saying:
#"AttributeError: 'bool' object has no attribute 'all'. i think it's because of "mymap" which was not taken as a ready-to-use matrix
#
# rows = int(input("# of rows "))
# cols = int(input("# of cols "))
#
# mymap = [0] * rows
# for i in range(0, rows):
#     mymap[i] = [0] * cols
# for i in range(0, rows):
#     for j in range(0, cols):
#         mymap[i][j] = input("enter each element and press enter ")

mymap = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0],
 [0,0,0,0]]

print ("this is your map: ", mymap)

import numpy as np
a = np.array(mymap)
print(a[~(a==0).all(1)])