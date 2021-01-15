n = int(input())
a = list(map(int, input().split()))
print(n*(n+1)//2 - sum(a))