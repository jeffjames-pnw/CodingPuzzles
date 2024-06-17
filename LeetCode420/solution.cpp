// https://leetcode.com/problems/strong-password-checker/description/
// Accepted

class Solution {
public:
    int strongPasswordChecker(string password) {
        // determine our violations        
        int lengthDelete = password.length() - 20;
        if (lengthDelete < 0) { lengthDelete = 0; }
        int lengthAdd = 6 - password.length();
        if (lengthAdd < 0) { lengthAdd = 0; }

        bool hasLower=false, hasUpper=false, hasDigit=false;
        int repeatCount = 0;
        int repeatCounts[51];
        char repeatLast = 0;
        for (int i = 0; i <= 50; i++) { repeatCounts[i] = 0; }
        for (int i = 0; i < password.length(); i++)
        {
            char c = password[i];
            if ('a' <= c && c <= 'z') { hasLower = true; }
            if ('A' <= c && c <= 'Z') { hasUpper = true; }
            if ('0' <= c && c <= '9') { hasDigit = true; }

            if (c == repeatLast) { repeatCount++; } 
            else {
                repeatLast = c;
                if (repeatCount > 2) { repeatCounts[repeatCount]++; }
                repeatCount = 1;
            }
        }
        if (repeatCount > 2) { repeatCounts[repeatCount]++; }
        int maxRepeat = 50;
        while (repeatCounts[maxRepeat] == 0 & maxRepeat>2) { maxRepeat--; }
        
        int specialAddOrReplace = 0;
        if (!hasLower) { specialAddOrReplace++; }
        if (!hasUpper) { specialAddOrReplace++; }
        if (!hasDigit) { specialAddOrReplace++; }
        
        // be opportunistic about handling repeats
        int steps = 0;

        // 1. delete down to 20
        // 1a. first sets of 3: AAA to AA, AAAAAA to AAAAA->AAXAA
        // avoid 5,8,11 which can replace into pairs--reduce others down to this
        if (lengthDelete > 0)
        {
            for (int r = maxRepeat; r > 2; r--)
            {
                if (r % 3 == 0)
                {
                    while (lengthDelete > 0 && repeatCounts[r] > 0)
                    {
                        steps++;
                        lengthDelete--;
                        repeatCounts[r]--;
                        repeatCounts[r-1]++;
                    }
                }
                if (r == maxRepeat && 0 == repeatCounts[maxRepeat]) { maxRepeat--; }
            }
        }
        // 1b. then sets of 3 + (1,0)
        if (lengthDelete > 0)
        {
            for (int r = maxRepeat; r > 2; r--)
            {
                if (r % 3 != 2)
                {
                    while (lengthDelete > 0 && repeatCounts[r] > 0)
                    {
                        steps++;
                        lengthDelete--;
                        repeatCounts[r]--;
                        repeatCounts[r-1]++;
                    }
                }
                if (r == maxRepeat && 0 == repeatCounts[maxRepeat]) { maxRepeat--; }
            }
        }
        // 1c. delete from other repeats
        if (lengthDelete > 0)
        {
            for (int r = maxRepeat; r > 2; r--)
            {
                while (lengthDelete > 0 && repeatCounts[r] > 0)
                {
                    int deletable = r - 2;
                    if (deletable > lengthDelete) { deletable = lengthDelete; }
                    steps += deletable;
                    repeatCounts[r]--;
                    repeatCounts[r-deletable]++;
                    if (r == maxRepeat && 0 == repeatCounts[maxRepeat]) { maxRepeat--; }
                    lengthDelete -= deletable;
                }
            }
        }
        // 1d. all remaining deletes
        if (lengthDelete > 0)
        {
            steps += lengthDelete;
        }
        
        // 2. add up to six
        // 2a. to fix repeats
        if (lengthAdd > 0)
        {
            for (int r = maxRepeat; r > 2; r--)
            {
                while (lengthAdd > 0 && repeatCounts[r] > 0)
                {
                    steps++;
                    repeatCounts[r]--;
                    repeatCounts[r-2]++;
                    lengthAdd--;
                    if (specialAddOrReplace > 0) { specialAddOrReplace--; }
                    if (r == maxRepeat && 0 == repeatCounts[maxRepeat]) { maxRepeat--; }
                }
            }
        }
        // 2b. all other adds
        if (lengthAdd > 0)
        {
            steps += lengthAdd;
            if (specialAddOrReplace > lengthAdd) { specialAddOrReplace -= lengthAdd; }
            else if (specialAddOrReplace > 0) { specialAddOrReplace = 0; }
        }
        
        // 3. replace to eliminate remaining repeats
        for (int r = maxRepeat; r > 2; r--)
        {
            while (repeatCounts[r] > 0)
            {
                steps++;
                repeatCounts[r]--;
                repeatCounts[r-3]++; // AAAAA -> AAXAA
                if (specialAddOrReplace > 0) { specialAddOrReplace--; }
            }
        }

        if (specialAddOrReplace)
        {
            steps += specialAddOrReplace;
        }
        
        return steps;
    }
};