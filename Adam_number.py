n=int(input())
t=n
a=n*n
rev=0
rev1=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
b=rev*rev
while b>0:
    r1=b%10
    rev1=rev1*10+r1
    b=b//10
if rev1==a:
    print("True")
else:
    print("False")