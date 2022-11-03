n = int(input())
sq = n * n 
s = 0
while sq > 0:
    r = sq % 10
    sq = sq // 10
    s += r
if (s == n):
    print('Neon Number')
else:
    print('Not Neon Number')