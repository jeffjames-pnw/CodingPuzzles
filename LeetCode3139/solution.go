// https://leetcode.com/problems/minimum-cost-to-equalize-array
// Wrong Answer, 579 / 636 testcases passed

const infinity = int(^uint(0) >> 1) // infinity
func minCostToEqualizeArray(nums []int, cost1 int, cost2 int) int {
	best := infinity
	total := best - 1
	target := max(nums)
	// keep trying so long as the total is going down
	for total < best {
		best = total
		total = try(nums, cost1, cost2, target)
		// fmt.Printf("target=%d total=%d\n", target, total)
		target += 1
	}
	return best
}
func max(nums []int) int {
	m := 0
	for _, x := range nums {
		if x > m {
			m = x
		}
	}
	return m
}
func show(nums []int) string {
	var ss []string
	for _, i := range nums {
		ss = append(ss, strconv.Itoa(i))
	}
	return strings.Join(ss, ",")
}
func copyarray(num []int) []int {
	result := make([]int, len(num))
	for i, v := range num {
		result[i] = v
	}
	return result
}
func try(nums []int, cost1 int, cost2 int, target int) int {
	total := 0
	sorted := copyarray(nums)
	sort.Ints(sorted)
	// if cost1 is always cheaper or necessary
	if cost1 <= int(cost2/2) || len(sorted) <= 2 || sorted[1] == target {
		// fmt.Printf("cost1=%d before=%s", cost1, show(sorted))
		for _, x := range sorted {
			total += cost1 * (target - x)
		}
		// fmt.Printf(" after=%s total=%d\n", show(sorted), total)
		return total
	}
	for sorted[0] < target && sorted[1] < target {
		// fmt.Printf("cost2=%d before=%s", cost2, show(sorted))
		// two increments while keeping the list sorted
		last := 1
		for last < len(sorted)-1 && sorted[1] == sorted[last+1] {
			last += 1
		}
		sorted[last] += 1
		last = 0
		for last < len(sorted)-1 && sorted[0] == sorted[last+1] {
			last = last + 1
		}
		sorted[last] = sorted[last] + 1
		total = total + cost2
		// fmt.Printf(" after=%s total=%d\n", show(sorted), total)
	}
	if sorted[0] < target {
		total = total + (target-sorted[0])*cost1
		// fmt.Printf("cost1=%d before=%s total=%d\n", cost1, show(sorted), total)
	}
	return total
}
