n=[1,2,3,4,5,6,7]
if len(n)<3:
    print(-1) 
first=second=third=float('-inf')
for i in n:
    if i>first:
        third=second
        second=first
        first=i
    elif i>second and i!=first:
        third=second
        second=i
    elif i>third and i!=first and i!=second:
        third=i

        
if third==float('-inf'):
    print('-1')
else:
    print(third)

