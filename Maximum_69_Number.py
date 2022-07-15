n=input()
for i in range (len(n)):
    if n[i]=='6':
        break
t="9"
n=n[0:i]+t+n[i+1:]
print(n)