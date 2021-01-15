n = int(input())
if n<4 and n>1:
    print("NO SOLUTION")
else:
    a = [0]*n
    t = n
    c = 0
    if n%2==0:
        t-=1
    for i in range(t, 0, -2):
        a[c] = i
        c+=1
    if n%2:
        n-=1
    for i in range(n, 1, -2):
        #print(i, c)
        a[c]=i
        c+=1
    print(*a)