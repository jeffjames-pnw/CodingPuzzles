# https://leetcode.com/problems/block-placement-queries/description/
# Time Limit Exceeded, 738 / 744 testcases passed

class Solution:
    def place(self, obstacles: [], item: int):
        left,right = 0,len(obstacles)
        while right > left:
            mid = int((left+right)/2)
            if item < obstacles[mid]:
                right = mid
            elif left < mid:
                left = mid
            else:
                left = mid+1
        obstacles.insert(left, item)
    def test(self, obstacles: [], limit: int, size: int) -> bool:
        left = 0
        for right in obstacles:
            if right > limit:
                right = limit
            space = right - left
            if space >= size:
                return True
            left = right
        if left < limit:
            space = limit - left
            if space >= size:
                return True
        return False
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = [] # List[int]
        result = [] # List[bool]
        for query in queries:
            if query[0] == 1:
                self.place(obstacles, query[1])
            elif query[0] == 2:
                result.append(self.test(obstacles, query[1], query[2]))
        return result