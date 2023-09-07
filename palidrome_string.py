def palidrome(s):
    if len(s)==0:
        return s
    d=palidrome(s[1:])+s[0]
    return d
s=str(input())
d=palidrome(s)
if d==s:
    print("this is a palidrome")
else:
    print("this is not palidrome")