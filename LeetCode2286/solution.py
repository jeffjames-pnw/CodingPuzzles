# https://leetcode.com/problems/booking-concert-tickets-in-groups/description/
# Time Limit Exceeded, 91 / 97 testcases passed
class BookMyShow:
    rowNext = []
    seatsPerRow = 0
    def __init__(self, n: int, m: int):
        self.rowNext = [0] * n
        self.seatsPerRow = m
    def gather(self, k: int, maxRow: int) -> List[int]:
        for row in range(0, maxRow+1):
            c = self.rowNext[row]
            if c + k <= self.seatsPerRow:
                self.rowNext[row] += k
                return [row, c]
        return []
    def scatter(self, k: int, maxRow: int) -> bool:
        plan = [0] * (maxRow+1)
        for row in range(0, maxRow+1):
            remain = self.seatsPerRow - self.rowNext[row]
            if remain >= k:
                plan[row] = k
                for i in range(maxRow+1):
                    self.rowNext[i] += plan[i]
                return True
            plan[row] = remain
            k -= remain
        return False