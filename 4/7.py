n = int(input())
f = 1
s = 0
for i in range(1, n + 1):
    f *= i
    s += f
print(s)