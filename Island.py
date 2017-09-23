def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    sum = 0
    for row, aRow in enumerate(grid):
        for col, val in enumerate(aRow):
            if val == 1:
                # top
                if row == 0:
                    sum = sum + 1
                elif grid[row-1][col] != 1:
                    sum = sum + 1

                # right
                if col == len(aRow)-1:
                    sum = sum + 1
                elif grid[row][col+1] != 1:
                    sum = sum +1

                # bottom
                if row == len(grid)-1:
                    sum = sum + 1
                elif grid[row+1][col] != 1:
                    sum = sum + 1

                # left
                if col == 0:
                    sum = sum + 1
                elif grid[row][col-1] != 1:
                    sum = sum + 1


    return sum


grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

print(islandPerimeter(grid))