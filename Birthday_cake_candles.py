
def tallest_candle(candles):
    # 1. find the maximum height of the candle you can use max() method
    maxi=candles[0]
    for num in candles:
        if(num>maxi):
            maxi=num
    # 2. count the maxi
    cnt=0
    for num in candles:
        if(num==maxi):
            cnt+=1

    return cnt
    


n=int(input())
candles=list(map(int,input().split()))
ans=tallest_candle(candles)
print(ans)


