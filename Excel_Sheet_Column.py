n=int(input())
o=''
while(n):
    i=(n-1)%26
    o+=chr(i+65)
    n=(n-1)//26
print(o[::-1])