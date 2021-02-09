n = int(input())
sum_ = n*(n+1)//2
if sum_%2:
    print("NO")
else:
    r1, r2 = [], []
    sum_//=2
    while n:
        if sum_ - n>=0:
            r1.append(n)
            sum_-=n
        else:
            r2.append(n)
        n-=1
    print("YES", len(r1), sep = '\n')
    print(*r1, sep = ' ')
    print(len(r2))
    print(*r2, sep = ' ')