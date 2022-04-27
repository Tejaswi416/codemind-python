a,b=map(int,input().split())
a=str(a)
t=a[:b]
t=int(t)
v=len(a)
v=a[v-b:]
v=int(v)
print(abs(t-v))