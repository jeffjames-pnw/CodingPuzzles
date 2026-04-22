# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/description/
#
# [1] maintain a list of remaining choices, reduced as we go
# [2] the k index must skip over unused instances of that choice k * (n-1)!
# then repeat until n choices made
#
# Submit Accepted!

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # remaining choices, reduced as we go
        choices = ""
        for i in range(1,n+1):
            choices = choices + str(i)
        # our answer, accumulated as we go
        answer = ""
        # zero-based
        k = k - 1
        while n > 0:
            # chunk to index & eliminate for current factorial
            chunk = math.factorial(n-1)
            next = int(k/chunk)
            answer = answer + choices[next]
            # print(f"n={n} k={k} choices={choices} chunk={chunk} next={next} answer={answer}")
            choices = choices[:next] + choices[next+1:]
            k = k - chunk * next
            n = n - 1
        return answer