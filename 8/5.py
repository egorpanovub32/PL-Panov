#5.1
# from random import randint
#
# N, M = map(int,input().split()) #размеры матрицы
# a = [[randint(-50, 50) for _ in range(M)] for _ in range(N)] #генерация чисел в матрице
# for i in a:
#     print(*sorted(i)) #вывод отсортированной матрицы


#5.2
# from random import randint
#
# N, M = map(int,input().split()) #размеры матрицы
# lst = [[randint(-50, 50) for _ in range(M)] for _ in range(N)] #создание матрицы
#
# print(lst) # вывод изначальной матрицы
#
# print(list([(1 if min(i) % 2 else 0)if j == min(i) else j for j in i] for i in lst)) #вывод измененой матрицы
