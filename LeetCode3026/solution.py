# https://leetcode.com/problems/maximum-good-subarray-sum/description/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        sum = 0
        max = -9223372036854775808 # -sys.maxint-1
        found = False
        for left in range(l):
            sum = nums[left]
            for right in range(left+1,l):
                sum += nums[right]
                if k == abs(nums[right] - nums[left]) and sum > max:
                    max = sum
                    found = True
        if not found:
            return 0
        return max