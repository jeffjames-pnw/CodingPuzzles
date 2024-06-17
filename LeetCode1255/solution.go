// https://leetcode.com/problems/maximum-score-words-formed-by-letters/
// Accepted

func contains(letters []byte, letter byte) (bool, []byte) {
	for i, l := range letters {
		if l == letter {
			j := i + 1
			return true, slices.Concat(letters[0:i], letters[j:])
		}
	}
	return false, letters
}
func maxScoreWords(words []string, letters []byte, score []int) int {
	bestScore := 0
	for _, word := range words {
		letters1 := letters
		wordScore := 0
		wordGood := true
		for wi := 0; wi < len(word); wi++ {
			wc := word[wi]
			good, letters2 := contains(letters1, word[wi])
			if good {
				letters1 = letters2
				wordScore = wordScore + score[wc-'a']
			} else {
				wordGood = false
				wordScore = 0
			}
		}
		// fmt.Printf("first=%s [%d] %s=%d letters=%d\n", words[0], i, word, wordScore, len(letters))
		if wordGood {
			arrayScore := wordScore + maxScoreWords(words[1:], letters1, score)
			if arrayScore > bestScore {
				bestScore = arrayScore
				// fmt.Printf("best=%d\n", bestScore)
			}
		}
	}
	return bestScore
}