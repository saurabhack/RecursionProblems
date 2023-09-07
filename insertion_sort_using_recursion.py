"""arr=list(map(int,input().split()))
for i in range(1,len(arr)):
    temp=arr[i]
    j=i-1
    while j>=0 and arr[j]>temp:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=temp
print(arr)"""

def insertionsort(arr,n):
    if n==0:
        return n

    insertionsort(arr,n-1)
    key=arr[n]
    j=n-1
    while j>=0 and key < arr[j]:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

arr=[2,5,1,3,4]
n=len(arr)
insertionsort(arr,n-1)
print(arr)