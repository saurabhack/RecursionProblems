def partition(arr,s,e):
    key=arr[s]
    counter=0
    for i in range(s+1,e+1):
        if arr[i]<=key:
            counter+=1
    index=s+counter
    arr[index],arr[s]=arr[s],arr[index]
    i=0
    j=e
    while i<index and j>index:
        while arr[i]<=key:
            i+=1
        while arr[j]>=key:
            j-=1
        if i<=index and j>index:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return index
def QuickSort(arr,s,e):
    if s>=e:
        return
    p=partition(arr,s,e)
    QuickSort(arr,s,p-1)
    QuickSort(arr,p+1,e)
arr=[10 ,28 ,38 ,38 ,41 ,57 ,79 ,91]
n=len(arr)-1
QuickSort(arr,0,n)
print(arr)