def linear(arr,n):
    key=8
    if n==0:
        return n
    if arr[n-1]==key:
        return n
    linear(arr,n-1)


arr=[2,1,3,4,5,6,7,10,8]
n=len(arr)
linear(arr,n)
print(linear(arr,n))
