def prime(a):
    if a==1:
        return False
    for i in range(2,int(a**.5)+1):
        if a%i==0:
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i)==1:
        print(i)