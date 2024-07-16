# https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/description/

class WrongSolution:
    def minimumCost(self, nums: List[int]) -> int:
        average = round((0.0 + sum(nums)) / len(nums))
        deviation = 0
        for i in nums:
            deviation += abs(average - i)
        return deviation

# Wrong Answer: 469 / 648 testcases passed
class Solution:
    def forcePalindromic(self, s: string) -> int:
        l = len(s)
        a = list(s)
        for i in range(0,int(l/2)):
            a[-1-i] = a[i]
        return int("".join(a))
        # single digit -> self
        # 10->9/11, 12-16 -> 11, 17-21 -> 22
        # 20-21->22<-23-27,28-32->33

    def nearestPalindromics(self, n: int) -> [int]:
        s = str(n)
        l = len(s)
        best = [self.forcePalindromic(s)]
        if s[0] == '1' and l > 1:
            s2 = '9' * (l-1)
            best.append(self.forcePalindromic(s2))
        if s[0] == '9':
            s2 = '1' + ('0' * (l-1)) + '1'
            best.append(self.forcePalindromic(s2))
        return best

    def minimumCost(self, nums: List[int]) -> int:
        average = round((0.0 + sum(nums)) / len(nums))
        targets = self.nearestPalindromics(average)
        for n in nums:
            targets += self.nearestPalindromics(n)
        best = 9223372036854775808
        for target in set(targets):
            deviation = 0
            for n in nums:
                deviation += abs(target - n)
            print(f"target={target} deviation={deviation}")
            if deviation < best:
                best = deviation
        return best
