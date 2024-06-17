// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/description/
// Time Limit Exceeded, 513 / 553 testcases passed

func findMaximumLength(a []int) int {
	l := len(a)
	if l < 2 {
		return l
	}
	one := a[0]
	two := a[1]
	index := 2
	rest := 0
	// [one, two, rest...]
	for i := index; i < l; i++ {
		rest += a[i]
	}
	return helper(a, one, two, index, rest)
}
func helper(a []int, one int, two int, index int, rest int) int {
	if one > two+rest {
		// fmt.Printf("cut(%d,%d,%d)=%d\n", one, two, rest, 1)
		return 1 // just one+two+rest
	}
	if rest == 0 {
		// fmt.Printf("cut(%d,%d,%d)=%d\n", one, two, rest, 2)
		return 2 // just one,two
	}
	three := a[index] // pop three off of rest
	rest -= three
	index += 1
	best := 0
	if one <= two { // step over one
		// fmt.Printf("step(%d,%d,%d)\n", one, two, three)
		best = 1 + helper(a, two, three, index, rest)
	}
	maybe := 2 + len(a) - index // i don't trust this
	average := int((one + two + three + rest) / one)
	if maybe > average {
		maybe = average
	}
	if best < maybe {
		// fmt.Printf("right(%d,%d) maybe=%d\n",one,two+three, maybe)
		right := helper(a, one, two+three, index, rest)
		if right > best {
			best = right
		}
	}
	if best < maybe {
		// fmt.Printf("left(%d,%d) maybe=%d\n",one+two, three, maybe)
		left := helper(a, one+two, three, index, rest)
		if left > best {
			best = left
		}
	}
	if best == 0 {
		fmt.Printf("error(%d,%d,%d,%d\n", one, two, three, rest)
	}
	return best
}