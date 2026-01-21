#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        original=n
        string=str(n)
        m=len(string)
        summ=0
        for i in range(m):
            digit=n%10
            summ+=digit**m
            n//=10
        return summ==original
            
            
