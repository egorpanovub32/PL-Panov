# 5.1
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# chisl = A * D + B * C #нахождение общего числителя
# znam = B * D #нахождение общего знаменателя
# a, b = chisl, znam
# while a != b: # алгоритм Евкалида
#     if a > b:
#         a -= b
#     else:
#         b -= a
# print(f'{chisl // a}/{znam // a}') # вывод несократимой дроби

# 5.2
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")