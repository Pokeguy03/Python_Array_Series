from typing import List

def printDivisors(n: int) -> List[int]:
    
    li=[]
    for i in range(1,n+1):
        if n%i==0:
            li.append(i)
    return li
