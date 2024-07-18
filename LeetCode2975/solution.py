<#
https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/
2975. Maximum Square Area by Removing Fences From a Field

There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) 
containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and
vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some 
fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) 
and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) 
and (1, n) to (m, n). These fences cannot be removed.

--

Put differently...
Find fences that make a square
x: 1,x,n -> check y for gaps of (x-1) or (n-x)

--
Wrong Answer 608 / 648 testcases passed
y1=26389 y2=136759 ygap=110370
x1=110472 x2=102 xgap=110370
gap=110370 in ygaps
12181536900 Output 
181536816 Expected
But 13473 * 13473 = 181521729 
#>


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        ygaps = set([m-1])
        for i, y1 in enumerate(hFences): # 1 < y1 < mn
            ygaps.add(abs(y1 - 1))
            ygaps.add(abs(y1 - m))
            for y2 in hFences[i+1:]:
                ygaps.add(abs(y1 - y2))
        xgaps = set([n-1])
        for i, x1 in enumerate(vFences): # 1 < x1 < n
            xgaps.add(abs(x1 - 1))
            xgaps.add(abs(x1 - n))
            for x2 in vFences[i+1:]:
                xgaps.add(abs(x1 - x2))
        for gap in reversed(sorted(xgaps)):
            if gap in ygaps:
                return gap * gap
        return -1