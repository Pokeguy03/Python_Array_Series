class Solution:
    def isPalindrome(self, n):
		# code here
		m=str(n)[::-1]
		inp=int(m)
		if n==inp:
		    return True
		return False



def isPalindrome(n: int) -> bool:
    if n < 0:
        return False   # negative numbers can't be palindromes

    original = n
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    return original == rev
