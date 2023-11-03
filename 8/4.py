# №1
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
s = []
for i in range(len(a)):
    s.append(sum(a[i]))
print("Строка с наибольшей суммой: ", a[s.index(max(s))])
print("Сумма элементов: ", max(s))
print("Строка с наименьшей суммой: ", a[s.index(min(s))])
print("Сумма элементов: ", min(s))



# №2
a = [[1, -5, 7], [-3, -1, 4], [6, 9, 2]]
for i in range(3):
    for j in range(3):
        if a[i][j] > 0:
            a[i][j] = 1
        elif a[i][j] < 0:
            a[i][j] = 0
print()
for i in range(3):
    for j in range(3):
        print(a[i][j], end=' ')
    print()

