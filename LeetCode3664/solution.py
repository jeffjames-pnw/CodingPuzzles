# 3664 Two-Letter Card Game
# https://leetcode.com/problems/two-letter-card-game/description/
#
# match by cases
# histogram for left & right: matches are min of (total-max, total/2)
# doubles can match with unpaired or previously matched
from collections import Counter
class Solution:
    def score(self, cards: List[str], x: str) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        doubles = 0
        for card in cards:
            if card[0] == x and card[1] == x:
                doubles += 1
            elif card[0] == x:
                left[card] += 1
            elif card[1] == x:
                right[card] += 1

        match_score = 0
        unpaired = 0

        # match same left with different right
        if len(left):
            total = sum(left.values())
            high = max(left.values())
            half = int(total/2)
            if high <= half:
                matches = half
            else:
                matches = total - high
            match_score += matches
            unpaired += total - 2*matches

        # match same right with different left
        if len(right):
            total = sum(right.values())
            high = max(right.values())
            half = int(total/2)
            if high <= half:
                matches = half
            else:
                matches = total - high
            match_score += matches
            unpaired += total - 2*matches
        
        doubles_score = 0
        # match doubles with unpaired
        matches = min(doubles, unpaired)
        doubles -= matches
        doubles_score += matches
        # unpaired -= matches

        # match doubles with previously matched
        matches = min(doubles, 2*match_score)
        half = int(matches/2)
        # doubles -= half
        
        return half + doubles_score + match_score
