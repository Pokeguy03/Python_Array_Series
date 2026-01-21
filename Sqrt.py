class Solution:
    def floorSqrt(self, n): 
        return int(n**0.5)



def floorSqrt(n: int) -> int:
    if n == 0 or n == 1:
        return n

    low, high = 1, n
    ans = 0

    while low <= high:
        mid = (low + high) // 2

        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid      # store possible answer
            low = mid + 1
        else:
            high = mid - 1

    return ans
