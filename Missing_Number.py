#Using Formula
class Solution:
    def missingNum(self, arr):
        n=len(arr)+1
        total=n*(n+1)//2
        sum=0
        for i in range (len(arr)):
            sum+=arr[i]
        return total-sum

#Using Hashmap
class Solution:
    def missingNumber(self, arr, n):
        freq = {}

        for num in arr:
            freq[num] = 1  

        for i in range(1, n + 1):
            if i not in freq:
                return i


