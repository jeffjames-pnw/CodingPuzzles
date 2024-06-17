# https://leetcode.com/problems/minimum-reverse-operations/
# Time Limit Exceeded, 694 / 711 testcases passed

class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        distance = [-2] * n
        distance[p] = 0
        for i in banned:
            distance[i] = -1
        remain = n - len(banned)
        last = [p]
        d = 0
        while len(last) > 0:
            # print(f"while next={next} distance={distance}")
            next = []
            d += 1
            for start in range(0, n-k+1):
                # print(f" d={d} start={start}")
                for p in last:
                    # print(f"  p={p}")
                    if start <= p and p < start+k:
                        new = (start + k - 1) - (p - start) # possibly non-optimal
                        # print(f"   new={new} distance[new]={distance[new]} distance={distance}")
                        if distance[new] == -2: # not been here before
                            distance[new] = d
                            next.append(new) # repeat from this position with d+1
            last = next
        for p in range(n):
            if distance[p] == -2:
                distance[p] = -1 # unreachable
        return distance