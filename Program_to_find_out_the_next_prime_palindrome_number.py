def is_prime(num):
    if num < 2:
        return False #not prime
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True #prime
def reverse(num):
    rev = 0
    while num > 0:
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    return rev

n = int(input())
n += 1
while True:
    if n == reverse(n) and is_prime(n) == True:
        print(n)
        break
    else:
        n += 1