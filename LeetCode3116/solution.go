// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
// Wrong Answer, 393 / 561 testcases passed

func findKthSmallest(coins []int, k int) int64 {
	coinCount := len(coins)
	sort.Ints(coins)
	// save last used count of these coins
	multiple := make([]int64, len(coins))
	for i := 0; i < coinCount; i += 1 {
		multiple[i] = 0
	}
	multiple[0] = int64(coins[0])
	var currentValue int64 = multiple[0]
	fmt.Printf("k=%d value=%d\n", k, currentValue)
	k -= 1
	for k > 0 {
		var nextValue int64 = multiple[0] + int64(coins[0])
		nextCoin := 0
		for i := 1; i < coinCount; i += 1 {
			value := multiple[i] + int64(coins[1])
			if currentValue < value && value < nextValue {
				nextValue = value
				nextCoin = i
			}
		}
		fmt.Printf("k=%d value=%d\n", k, nextValue)
		multiple[nextCoin] = nextValue
		currentValue = nextValue
		k -= 1
	}
	return currentValue
}