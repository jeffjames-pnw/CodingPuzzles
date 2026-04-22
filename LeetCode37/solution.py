# 37 Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/description/
#
# find the most constrained space and choose that
# this code does not guess yet
# passes basic test cases but not full suite

class Solution:
    def calcMove(self, y:int, x:int, board: List[List[str]]) -> int:
        vremain = [True] * 10 # 1-9 index by digit, ignoring [0]
        cy = y - (y%3)
        cx = x - (x%3)
        for z in range(0,9):
            v = board[y][z]
            if v != ".":
                vremain[int(v)] = False
            v = board[z][x]
            if v != ".":
                vremain[int(v)] = False
            dy = int(z/3)
            dx = z % 3
            v = board[cy+dy][cx+dx]
            if v != ".":
                vremain[int(v)] = False
        remain = 0
        last = 0
        for z in range(1,10):
            if vremain[z]:
                remain = remain + 1
                last = z
        if remain == 1:
            return last
        return 0
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty = 1
        move = "something"
        while empty > 0 and move != "":
            empty = 0
            move = ""
            for y in range(0,9):
                for x in range(0,9):
                    if board[y][x] == ".":
                        empty = empty + 1
                        if move == "":
                            digit = self.calcMove(y,x,board)
                            if digit > 0:
                                move = f"calcMove({y},{x})={digit}"
                                board[y][x] = str(digit)
                                empty = empty - 1
            print(f"{move} empty={empty}")
