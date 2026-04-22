# 1855. Maximum Distance Between a Pair of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/
#
# leverage that the lists are non-increasing to binary search for the rightmost match for each left value
#
# Submit Accepted!

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        maximum = 0
        for i in range(len(nums1)):
            left = i+1
            right = len(nums2)-1
            j = left
            while (left < right):
                j = int((left+right+1)/2)
                if (nums1[i] <= nums2[j]):
                    left = j
                else:
                    right = j-1
                    j = right
            if i < j and j < len(nums2) and nums1[i] <= nums2[j]:
                distance = j - i
                if distance > maximum:
                    maximum = distance
        return maximum
