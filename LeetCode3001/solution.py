# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/description/

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # rook(a,b) bishop(c,d) queen(e,f)

        # can bishop can take queen?
        ediff = e - c
        fdiff = f - d
        if abs(ediff) == abs(fdiff):
            # is the rook in the way?
            adiff = a - c
            bdiff = b - d
            if abs(adiff) == abs(bdiff) and ((c < a and a < e) or (e < a and a < c)) and ((d < b and b < f) or (f < b and b < d)):
                        return 2
            else:
                return 1

        # can rook take queen directly?
        if a == e:
            if c == e and ((b < d and d < f) or (f < d and d < b)):
                # is bishop in the way?
                return 2
            else:
                return 1
        if b == f:
            if d == f and ((a < c and c < e) or (e < c and c < a)):
                # is bishop in the way?
                return 2
            else:
                return 1
        
        # otherwise move rook twice, evading bishop
        return 2
        

        
