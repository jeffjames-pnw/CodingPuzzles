// https://leetcode.com/problems/strong-password-checker/description/
// Accepted

func strongPasswordChecker(password string) int {
	l := len(password)
	add := 6 - l
	if add < 0 {
		add = 0
	}
	remove := l - 20
	if remove < 0 {
		remove = 0
	}
	hasDigit := false
	hasLower := false
	hasUpper := false
	longMod3 := []int{0, 0, 0}
	long3x := 0
	longChar := password[0]
	longCount := 0
	for i := 0; i < l; i++ {
		c := password[i]
		if '0' <= c && c <= '9' {
			hasDigit = true
		} else if 'a' <= c && c <= 'z' {
			hasLower = true
		} else if 'A' <= c && c <= 'Z' {
			hasUpper = true
		}
		if i > 0 && c == longChar { // same char
			longCount = longCount + 1
		} else {
			if longCount > 2 { // new char
				longMod3[longCount%3] = longMod3[longCount%3] + 1
				long3x = long3x + int(longCount/3) - 1
			}
			longChar = c
			longCount = 1
		}
	}
	if longCount > 2 {
		longMod3[longCount%3] = longMod3[longCount%3] + 1
		// xxXxxX -> 0,0   xxXxx -> 0,2   xxXx -> 0,1
		long3x = long3x + int(longCount/3) - 1
	}
	longMod3[2] = longMod3[2] + long3x
	steps := 0
	// use remove to satisfy longMod3
	// xxX    1%0  change 1 or remove 1
	// xxXx   1%1  change 1 or remove 2
	// xxXxx  1%2  change 1 or remove 3
	for _, mod := range []int{0, 1, 2} {
		for remove > mod && longMod3[mod] > 0 {
			steps = steps + mod + 1
			remove = remove - mod - 1
			longMod3[mod] = longMod3[mod] - 1
		}
	}
	// edge case: remove=1 longMod3[1]=1 xxXx
	// change 1 char, remove 1 elsewhere?
	steps = steps + remove // no other use for remove
	// use long correction to fulfill other needs
	// aaaa -> aaAaa9
	longChange := longMod3[2] + longMod3[1] + longMod3[0]
	hasChanges := 0
	if !hasDigit {
		hasChanges = hasChanges + 1
	}
	if !hasLower {
		hasChanges = hasChanges + 1
	}
	if !hasUpper {
		hasChanges = hasChanges + 1
	}
	// insert/change to satisfy add, longChange, hasChanges
	for add > 0 || longChange > 0 || hasChanges > 0 {
		steps = steps + 1
		if add > 0 {
			add = add - 1
		}
		if longChange > 0 {
			longChange = longChange - 1
		}
		if hasChanges > 0 {
			hasChanges = hasChanges - 1
		}
	}
	return steps
}
