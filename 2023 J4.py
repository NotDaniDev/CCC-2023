C = int(input())
ts = list(map(int, input().split()))
bs = list(map(int, input().split()))
ans = 0
for i in range(C):
    ans += 3 * (ts[i] + bs[i])
for i in range(C - 1):
    if ts[i] and ts[i + 1]:
        ans -= 2
    if bs[i] and bs[i + 1]:
        ans -= 2
for i in range(0, C, 2):
    if ts[i] and bs[i]:
        ans -= 2
print(ans)