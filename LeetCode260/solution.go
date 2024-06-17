// https://leetcode.com/problems/single-number-iii/?envType=daily-question&envId=2024-05-31
// Accepted

func singleNumber(nums []int) []int {
	var once []int
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	prior, count := nums[0], 0
	for _, element := range nums {
		if element == prior {
			count = count + 1
		} else {
			if count == 1 {
				once = append(once, prior)
			}
			prior = element
			count = 1
		}
	}
	if count == 1 {
		once = append(once, prior)
	}
	return once
}