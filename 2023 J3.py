n = int(input())
availability = [input() for _ in range(n)]

max_count = 0
max_days = []

for i in range(5):
    count = sum(1 for j in range(n) if availability[j][i] == 'Y')
    if count > max_count:
        max_count = count
        max_days = [i+1]
    elif count == max_count:
        max_days.append(i+1)

print(*max_days, sep=',')
