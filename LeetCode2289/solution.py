# https://leetcode.com/problems/steps-to-make-array-non-decreasing/description/

class Solution1:
    def totalSteps(self, nums: List[int]) -> int:
        peakValue = 0
        previousValue = 0
        deletions = 0
        maxDeletions = 0
        previousDecline = False
        for currentValue in nums:
            if currentValue >= peakValue: # rising above peak
                peakValue = currentValue
                if deletions > maxDeletions:
                    maxDeletions = deletions
                deletions = 0
                previousDecline = False
            elif currentValue >= previousValue: # below peak but rising
                deletions += 1
                previousDecline = False
            elif not previousDecline:
                previousDecline = True
                deletions += 1
            previousValue = currentValue
            # print(f"currentValue={currentValue} previousValue={previousValue} peakValue={peakValue} deletions={deletions} maxDeletions={maxDeletions} previousDecline={previousDecline}")
        if deletions > maxDeletions:
            maxDeletions = deletions
        return maxDeletions
                
class Solution: # BruteForce:
    def totalSteps(self, nums: List[int]) -> int:
        result = 0
        deletions = True
        while deletions:
            deletions = False
            previous = nums[0]
            i = 1
            while i < len(nums):
                # print(f"i={i} nums[i]={nums[i]} previous={previous} deletions={deletions} result={result}")
                current = nums[i]
                if current < previous:
                    previous = nums[i]
                    del nums[i]
                    deletions = True
                else:
                    i += 1
                previous = current
            if deletions:
                result += 1
        return result
                