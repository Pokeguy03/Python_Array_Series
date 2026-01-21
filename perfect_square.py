class Solution:
    def isPerfect(self, n):
        # code here 
        if n<=1:
            return False
        summ=0
        for i in range(1,(n//2)+1):
            if n%i==0:
                summ+=i
        return True if n==summ else False
