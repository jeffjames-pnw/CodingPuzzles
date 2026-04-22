# 51. N-Queens
# https://leetcode.com/problems/n-queens/description/
#
# # pick() recursion takes past choices & constraint status
# enumerates through allowed next choices & recurses
#
# Submit Accepted!

class Solution:
    def pick(self, n: int, filledRows, cols, left, right):
        results = []
        row = len(filledRows)
        if row == n:
            return [filledRows]
        # col options for the queen in this row
        for col in range(n):
            ri = col+row
            li = n-1-col+row
            if cols[col] and right[ri] and left[li]:
                cols[col] = False
                right[ri] = False
                left[li] = False
                nextRow = "." * col + "Q" + "." * (n-1-col)
                results = results + self.pick(n, filledRows + [nextRow], cols, left, right)
                cols[col] = True
                right[ri] = True
                left[li] = True
        return results
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [True] * n
        left = [True] * (2*n-1)
        right = [True] * (2*n-1)
        return self.pick(n, [], cols, left, right)