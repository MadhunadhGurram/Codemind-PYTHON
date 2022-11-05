def pfs(num):
    fs=0
    for i in range(1,num):
        if num%i==0:
            fs+=i
    return fs

a=int(input())
b=int(input())
if (pfs(a)==b and pfs(b)==a):
    print("Amicable")
else:
    print("Not Amicable")