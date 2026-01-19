#method 1
ar=[1,2,3,4]
ar.reverse()
print(ar)

# #method 2
ar = [1, 2, 3, 4]
reverse = ar[::-1]
print(reverse)

#method 3
ar=[1,2,3,4]
left=0
right=len(ar)-1
while left < right:
    ar[left],ar[right]=ar[right],ar[left]
    left+=1
    right-=1
print(ar)

#For only integer:
class Solution:
	def reverseDigits(self, n):
	    rev=0
	    while n>0:
	        digit=n%10
	        rev=rev*10+digit
	        n//=10
	    return rev
