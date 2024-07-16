# https://leetcode.com/problems/divide-two-integers/description/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = False
        if dividend < 0:
            negative = not negative
            dividend = -dividend
        if divisor < 0:
            negative = not negative
            divisor = -divisor

        chunk = divisor
        count = 1
        while chunk <= dividend: # go too far
            chunk, count = chunk << 1, count << 1
            # print(f"dividend={dividend} chunk,count={chunk},{count}")
        chunk, count = chunk >> 1, count >> 1 # then back up
        
        result = 0
        while count >= 1:
            if dividend >= chunk:
                # print(f"dividend,result={dividend}-{result} chunk,count={chunk},{count}")
                dividend -= chunk
                result += count
            chunk, count = chunk >> 1, count >> 1

        if negative:
            result = -result
        if result == 2147483648:
            result -= 1
        return result

# pass1: non-optimized
class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        increment = 1
        if dividend < 0:
            increment = -increment
            dividend = -dividend
        if divisor < 0:
            increment = -increment
            divisor = -divisor
        result = 0
        while dividend >= divisor:
            dividend -= divisor
            result += increment
        return result