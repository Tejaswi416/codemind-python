a,b=map(int,input().split(':'))
t=30*a-5.5*b
t=abs(t)
if(t>180):
    print(360-t)
else:
    print(t)