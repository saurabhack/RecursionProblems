def helpme(d):
     if len(d)==1:
         return d
     l=int(d)
     add=0
     while l!=0:
         r=l%10
         add=add+r
         l=l//10
     d=str(add)

     m=helpme(d)
     return m
def recursiveDegits(n,k):
    if len(n)==1:
        return
    d=n*k
    return helpme(d)
n="9875"
k=4
print(recursiveDegits(n,k))
