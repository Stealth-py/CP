s = input()
n = len(s)
x = s[0]
ans = 1
t = 1
for i in range(1, n):
    if s[i]==s[i-1]:
        t+=1
    else:
        ans = max(t, ans)
        t = 1
ans = max(ans, t)
print(ans)