def merge(arr,s,e):
    mid=(s+e)//2
    first=arr[s:mid+1]
    second=arr[mid+1:e+1]
    i1=0
    i2=0
    i=s
    while(i1 < len(first) and i2<len(second)):
        if first[i1]<second[i2]:
            arr[i]=first[i1]
            i1+=1
            i+=1
        else:
            arr[i]=second[i2]
            i2+=1
            i+=1
    while( i1<len(first)):
        arr[i]=first[i1]
        i+=1
        i1+=1
    while(i2<len(second)):
        arr[i]=second[i2]
        i+=1
        i2+=1

def mergeSort(arr,s,e):
    if s>=e:
        return
    mid=(s+e)//2
    mergeSort(arr,s,mid)
    mergeSort(arr,mid+1,e)
    merge(arr,s,e)
    pass
arr=[4,2,1,3,5]
mergeSort(arr,0,len(arr)-1)
print(arr)