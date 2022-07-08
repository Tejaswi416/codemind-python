t=int(input())
while t:
    t-=1
    n=int(input())
    t=n
    su=0
    while n>0:
        r=n%10
        su=su*10+r
        n//=10
    if(su==t):
        print(True)
    else:
        print(False)