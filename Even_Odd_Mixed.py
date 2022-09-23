n=int(input())
x=0
y=0
while n>0:
    r=n%10
    if r%2==0:
        x+=1
    else:
        y+=1
    n=n//10
if x==0:
    print("Odd")
elif y==0:
    print("Even")
else:
    print("Mixed")