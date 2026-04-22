# 32 Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# simple solution of just parens depth misses ignoring to the left
# to fix that, left[] stack tracks the leftmost '(' at that depth
# so that '()(...' points to the first one and not the second
# going deeper than maxdepth says "nothing farther left, remember this one"
#
# Submit Accepted!

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = [0] * len(s)
        depth = 0
        maxdepth = 0
        longest = 0
        prior = 0
        for i in range(len(s)):
            if s[i] == '(':
                depth = depth + 1
                if depth > maxdepth:
                    left[depth-1] = i
                    maxdepth = depth
            elif s[i] == ')':
                if depth > 0:
                    maxdepth = depth
                    depth = depth - 1
                    length = 1 + i - left[depth]
                    if length > longest:
                        longest = length
                else:
                    maxdepth = 0
        return longest