class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 0
        right = x//2

        while left <= right:
            mid = left+(right-left) // 2
            val= mid*mid
            if val == x:
                return mid
            elif val < x:
                left = mid + 1  
            else:
                right = mid - 1
        return right
