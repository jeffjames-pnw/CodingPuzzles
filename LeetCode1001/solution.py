# 1001. Grid Illumination
# https://leetcode.com/problems/grid-illumination/description/
#
# store the grid plus constraints for rows, cols, and left and right diagonals
# pass 1 turns on the lamps and updates the constraints
# pass 2 answers the queries and turns off the lamps in the 3x3 around the query
#
# Submit Accepted!

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        results = []
        grid = [[False] * n] * n
        rows = [0] * n
        cols = [0] * n
        right = [0] * n
        left = [0] * n
        # turn on lamps
        for y in range(len(lamps)):
            for x in range(len(lamps[y])):
                grid[y][x] = True
                rows[y] = rows[y] + 1
                cols[x] = cols[x] + 1
                ri = x+y
                right[ri] = right[ri] + 1                
                li = n-1+x-y
                left[ri] = left[ri] +1
        # turn off lamps
        for y in range(len(queries)):
            for x in range(len(queries[y])): 
                q = grid[y][x] or rows[y]>0 or cols[x]>0 or right[x+y]>0 or left[n-1+x-y]>0
                results = results + [q]
                grid[y][x] = False
                for dy in (-1,0,1):
                    yy = y+dy
                    if 0<=yy and yy<n:
                        for dx in (-1,0,1):
                            xx = x + dx
                            if 0<=xx and xx<n:
                                grid[y][x] = True
                                rows[y] = rows[y] - 1
                                cols[x] = cols[x] - 1
                                ri = xx+yy
                                right[ri] = right[ri] - 1                
                                li = n-1+xx-yy
                                left[ri] = left[ri] - 1
        return results
