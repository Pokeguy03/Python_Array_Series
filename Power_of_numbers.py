#Method 1
class Solution:
    def reverseexponentiation(self, n):
        num=str(n)[::-1]
        inp=int(num)
        return n**inp

#Method 2
def power_of_reverse(n):
    temp = n
    rev = 0

    # reverse the number
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    # compute power
    return n ** rev


# Example
n = 2
print(power_of_reverse(n))
