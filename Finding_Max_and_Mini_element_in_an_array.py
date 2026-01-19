#Method 1 Brute force
arr=[5,2,3,9]
b=sorted(arr)
print(b[0])
print(b[-1])

#Method 2 
arr=[5,3,4,8,9,11]
mini=float('inf')
maxi=float('-inf')
for i in arr:
    if i<mini:
        mini=i
    if i>maxi:
        maxi=i
print(mini)
print(maxi)
