5.1
from random import randint
N, M = map(int,input("Введите размеры: ").split())
a = [[randint(-50, 50) for _ in range(M)] for _ in range(N)]
print(a)
print()
for i in a:
    print(*sorted(i))

5.2
from random import randint
N, M = map(int,input("Введите размеры: ").split())
a = [[randint(-50, 50) for _ in range(M)] for _ in range(N)]
print(a,end=" ")
print()
print(list([(1 if min(i) % 2 else 0)if j == min(i) else j for j in i] for i in a))
