// https://leetcode.com/problems/single-number-iii/?envType=daily-question&envId=2024-05-31
// Accepted

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> once;
        sort(nums.begin(), nums.end());
        int prior = *(nums.begin());
        int count = 0;
        for (auto i = nums.begin(); i != nums.end(); ++i)
        {
            if (*i == prior)
            {
                count++;
            }
            else
            {
                if (count == 1)
                {
                    once.push_back(prior);
                }
                prior = *i;
                count = 1;
            }
        }
        if (count == 1)
        {
            once.push_back(prior);
        }
        return once;
    }
};