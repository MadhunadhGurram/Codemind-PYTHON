def lcm(a, b):
    r=max(a,b)
    if r%a==0 and r%b==0:
        return r
    while r%a!=0 or r%b!=0:
        r+= max(a, b)
    return r

a, b = map(int, input().split())
print(lcm(a,b))