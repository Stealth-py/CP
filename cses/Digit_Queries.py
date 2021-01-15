for i in range(int(input())):
    n = int(input())
    x = n
    p = 9
    q = 1
    while x//q >= p:
        x -= p*q
        p *= 10
        q += 1
    if x%q==0:
        f = x//q - 1
        num = pow(10, q-1) + f
        numl = [int(i) for i in str(num)]
        print(numl[-1])
    else:
        f = x//q
        num = pow(10, q-1) + f
        rem = x % q
        numl = [int(i) for i in str(num)]
        print(numl[rem-1])