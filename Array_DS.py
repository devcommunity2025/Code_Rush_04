

def reverse_arr(arr):
    # you can also use reverse() method
    i=0
    j=len(arr)-1
    while(i<=j):
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1
        
    return arr 

n=int(input())
arr=list(map(int,input().split()))
res=reverse_arr(arr)
for num in res:
    print(num,end=" ")
