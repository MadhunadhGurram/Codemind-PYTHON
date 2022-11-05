n = int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    while n>=1:
        r=n%10
        c1=0
        for i in range(1,r+1):
            if r%i==0:
                c1+=1
        n=n//10
    if c1==2:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
        print("Not Mega Prime")