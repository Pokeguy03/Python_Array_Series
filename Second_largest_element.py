n=[5,3,4,9,7]
if len(n)<2:
    print(-1) 
first=second=float('-inf')
for i in n:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
        
if second==float('-inf'):
    print('-1')
else:
    print(second)

