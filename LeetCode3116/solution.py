# https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
# Wrong Answer: Case 1
class Solution:
    def countToValue(self, coins: List[int], max: int) -> int:
        count = int(max/coins[0])
        print(F"max={max} coin={coins[0]} alone={count} common=0 count={count}")
        for i in range(1, len(coins), 1):
            alone = int(max/coins[i])
            common = 0
            for j in range(0,i): # overlap with prior coins
                # max=14 coin=4 alone=3 common=4 count=8 - overcount
                overlap = lcm(coins[i], coins[j])
                common += int(max/overlap)
                for k in range(0,j): # minus its overlap with prior coins
                    double = lcm(coins[j], coins[k])
                    print(f"first={coins[i]} second={coins[j]} overlap={overlap}, third={coins[k]} double={double}")
                    common -= int(max/double)
                # max=6 coin=9 alone=0 common=-1 count=3
                # 3: 3,6,9 - alone=3 common=0
                # 6: 6 - alone=1 common=1 count+=0
                # 9: 9 - alone=1 common=1
                # first=9 second=6 overlap=18, third=3 double=6
                # max=6 coin=9 alone=0 common=-1 count=3
            count += alone - common
            print(F"max={max} coin={coins[i]} alone={alone} common={common} count={count}")
        return count
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coinCount = len(coins)
        coins = sorted(coins)
        lower = coins[0]
        upper = coins[0] * k
        while lower < upper:
            middle = int((lower+upper)/2) # round up
            count = self.countToValue(coins, middle)
            print(f"coins={coins} target={k} current={count} range: lower={lower} middle={middle} upper={upper} \n")
            if count < k and lower != middle:
                lower = middle
            elif count < k:
                lower = middle + 1
            else:
                upper = middle
        return lower