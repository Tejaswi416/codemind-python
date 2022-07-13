P,R,T=map(float,input().split())
ci=P*(pow((1 + R / 100),T))
print(format(ci,'.2f'))