// https://leetcode.com/problems/single-number-iii/?envType=daily-question&envId=2024-05-31
// Accepted

public class Solution {
    public int[] SingleNumber(int[] nums) {
        List<int> once = new List<int>();
        Array.Sort(nums);
        int prior = nums[0];
        int count = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (nums[i] == prior)
            {
                count++;
            }
            else
            {
                if (count == 1)
                {
                    once.Add(prior);
                }
                prior = nums[i];
                count = 1;
            }
        }
        if (count == 1)
        {
            once.Add(prior);
        }
        return once.ToArray();
    }
}