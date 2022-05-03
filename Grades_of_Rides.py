h,s,sp=map(int,input().split())
if h>50 and s>60 and sp>100:
    grade="10"
elif h>50 and s>60:
    grade="9"
elif s>60 and sp>100:
    grade="8"
elif h>50 and sp>100:
    grade="7"
elif h>50:
    grade="6"
else:
    grade="5"
print(grade)