<#
https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/description/
2202. Maximize the Topmost Element After K Moves

You are given a 0-indexed integer array nums representing the contents of a pile, 
where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:
- If the pile is not empty, remove the topmost element of the pile.
- If there are one or more removed elements, add any one of them back onto the pile. 
  This element becomes the new topmost element.

You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. 
In case it is not possible to obtain a non-empty pile after k moves, return -1.

--

Accepted submitted at Jul 18, 2024 14:58

#>

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        max = -1
        i = 0
        # parity prevents non-zero
        if len(nums) == 1 and k % 2 == 1:
            return -1
        # for i = 8, remove 7 items, return highest as 8th
        while i < k-1 and i < len(nums):
            if nums[i] > max:
                max = nums[i]
            i += 1
        # cannot land on that k-1th item
        # can take the kth item to reveal the k+1th value
        if len(nums) > k:
            if nums[k] > max:
                max = nums[k]
        return max