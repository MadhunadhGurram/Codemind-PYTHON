n=int(input())
a=n
while True:
    is_prime=True
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            is_prime=False
            break
    if is_prime == True:
        print("prime")
        break
    else:
        print("not a prime")
        break