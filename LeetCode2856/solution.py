<#
https://leetcode.com/problems/minimum-array-length-after-pair-removals/description/

Given an integer array num sorted in non-decreasing order.

You can perform the following operation any number of times:

Choose two indices, i and j, where nums[i] < nums[j].
Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
Return the minimum length of nums after applying the operation zero or more times.

Approach
Calculate histogram
Take from highest and lowest
Resort
Repeat
#>

# Accepted submitted at Jul 18, 2024 11:08
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        increasing = sorted(counts.keys(), key=lambda k: counts[k])
        farleft = 0
        farright = len(increasing)-1
        while farleft < farright:
            left = increasing[farleft]
            counts[left] -= 1
            if counts[left] == 0:
                farleft += 1
            right = increasing[farright]
            counts[right] -= 1
            if counts[right] == 0:
                farright -= 1
            elif farleft < farright and counts[right] < counts[increasing[farright-1]]:
                swapright = farright-1
                swapleft = farleft
                while swapleft < swapright:
                    swapmiddle = int((swapleft + swapright)/2)
                    if counts[right] < counts[increasing[swapmiddle]]:
                        swapright = swapmiddle
                    else:
                        swapleft = swapmiddle + 1
                increasing[farright] = increasing[swapright]
                increasing[swapright] = right
        if len(increasing) > 0:
            return counts[increasing[farleft]]
        else:
            return 0

# Time Limit Exceeded 629 / 636 testcases passed
class ThirdOptimization:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        increasing = sorted(counts.keys(), key=lambda k: counts[k])
        farleft = 0
        farright = len(increasing)-1
        while farleft < farright:
            left = increasing[farleft]
            counts[left] -= 1
            if counts[left] == 0:
                farleft += 1
            right = increasing[farright]
            counts[right] -= 1
            if counts[right] == 0:
                farright -= 1
            else:
                swap = farright
                while counts[right] < counts[increasing[swap-1]]:
                    swap -= 1
                if swap != farright:
                    increasing[farright] = increasing[swap]
                    increasing[swap] = right
        if len(increasing) > 0:
            return counts[increasing[farleft]]
        else:
            return 0

# Time Limit Exceeded 629 / 636 testcases passed
class SecondOptimization:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        increasing = sorted(counts.keys(), key=lambda k: counts[k])
        farleft = 0
        farright = len(increasing)-1
        while farleft < farright:
            left = increasing[farleft]
            counts[left] -= 1
            if counts[left] == 0:
                farleft += 1
            right = increasing[farright]
            counts[right] -= 1
            if counts[right] == 0:
                farright -= 1
            elif counts[right] < counts[increasing[farright-1]]:
                increasing = sorted(increasing[farleft:farright+1], key=lambda k: counts[k])
                farleft = 0
                farright = len(increasing)-1
        if len(increasing) > 0:
            return counts[increasing[farleft]]
        else:
            return 0

# Time Limit Exceeded 623 / 636 testcases passed
class InitialOptimization:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        increasing = sorted(counts.keys(), key=lambda k: counts[k])
        while len(increasing) > 1:
            left = increasing[0]
            counts[left] -= 1
            if counts[left] == 0:
                increasing = increasing[1:]
            right = increasing[-1]
            counts[right] -= 1
            if counts[right] == 0:
                increasing = increasing[:-1]
            increasing = sorted(increasing, key=lambda k: counts[k])
        if len(increasing) > 0:
            return counts[increasing[0]]
        else:
            return 0

class FirstPass:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        
        increasing = sorted(counts.keys(), key=lambda k: counts[k])
        ileft = 0
        left = increasing[ileft]
        iright = len(counts)-1
        right = increasing[iright]
        while ileft < iright:
            counts[left] -= 1
            if counts[left] == 0:
                ileft += 1
                left = increasing[ileft]
            counts[right] -= 1
            if counts[right] == 0:
                iright -= 1
                right = increasing[iright]
        return counts[left]
    
