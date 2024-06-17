// https://leetcode.com/problems/block-placement-queries/description/
// Time Limit Exceeded, 741 / 744 testcases passed

func getResults(queries [][]int) []bool {
	obstacles := []int{}
	result := []bool{}
	for _, query := range queries {
		if query[0] == 1 {
			obstacles = place(obstacles, query[1])
		} else if query[0] == 2 {
			result = append(result, test(obstacles, query[1], query[2]))
		}
	}
	return result
}
func place(obstacles []int, onew int) []int {
	for i, oold := range obstacles {
		if oold > onew {
			// insert
			obstacles = append(obstacles, 0)     // increase allocation
			copy(obstacles[i+1:], obstacles[i:]) // shift right
			obstacles[i] = onew
			return obstacles
		}
	}
	// append
	return append(obstacles, onew)
}
func test(obstacles []int, limit int, size int) bool {
	left := 0
	for _, right := range obstacles {
		if right > limit {
			right = limit
		}
		space := right - left
		if space >= size {
			return true
		}
		left = right
	}
	if left < limit {
		space := limit - left
		if space >= size {
			return true
		}
	}
	return false
}