
def odd_occur(l):
    # 1. store the frequency of each element 
    dict={} 
    for num in l:
        dict[num]=0
    for num in l:
        dict[num]+=1
    # 2. key is element and value is frequency. So if freq is 3 i.e odd then return the num (key)    
      
    for k in dict:
        if(dict[k]%2!=0):
             return k


n=int(input())
l=list(map(int,input().split()))
res=odd_occur(l)
print(res)