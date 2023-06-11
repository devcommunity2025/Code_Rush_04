
def change(x):
    cost=x
    bal=100
    rem=cost%10
    if(rem<=5):
        cost=cost-rem
    else:
        cost=cost +(10-rem)
    bal=100-cost
    
    return bal


x=int(input())
res=change(x)
print(res)