# https://leetcode.com/problems/strong-password-checker/description/
# Accepted

import array
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        l = len(password)
        add = 6 - l
        if add < 0:
            add = 0
        remove = l - 20
        if remove < 0:
            remove = 0
        hasDigit = False
        hasLower = False
        hasUpper = False
        longMod3 = [0,0,0]
        long3x = 0
        longChar = password[0]
        longCount = 0
        # find issues in the current password
        for i in range(l):
            c = password[i]
            if '0' <= c and c <= '9':
                hasDigit = True
            elif 'a' <= c and c <= 'z':
                hasLower = True
            elif 'A' <= c and c <= 'Z':
                hasUpper = True
            if i > 0 and c == longChar:
                longCount = longCount + 1
            else:
                if longCount > 2:
                    longMod3[longCount % 3] += 1
                    long3x += int(longCount/3) - 1
                longChar = c
                longCount = 1
        if longCount > 2:
            longMod3[longCount % 3] += 1
            long3x += int(longCount/3) - 1
        longMod3[2] += long3x
        # now prescribe how to resolve those issues
        steps = 0
        # remove repeated characters along with excess
        for mod in range(3):
            while remove > mod and longMod3[mod] > 0:
                steps += mod + 1
                remove -= mod + 1
                longMod3[mod] -= 1
        # remaining excess must be deleted, no overlap 
        steps = steps + remove
        # remaining repeats can be doubled up with adds/changes
        longChange = longMod3[0]+longMod3[1]+longMod3[2]
        hasChanges = 0
        if not hasDigit:
            hasChanges += 1
        if not hasLower:
            hasChanges += 1
        if not hasUpper:
            hasChanges += 1
        while add > 0 or longChange > 0 or hasChanges > 0:
            steps += 1
            if add > 0:
                add -= 1
            if longChange > 0:
                longChange -= 1
            if hasChanges > 0:
                hasChanges -= 1
        return steps
