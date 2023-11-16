#4.1
a = [[1, 6, 8, 12], [9, 7, 7, 2], [3, 10, 13, 2]]
s = []
for i in range(len(a)):
    s.append(sum(a[i]))
print("Строка с наибольшей суммой: ", a[s.index(max(s))])
print("Сумма элементов: ", max(s))
print("Строка с наименьшей суммой: ", a[s.index(min(s))])
print("Сумма элементов: ", min(s))



#4.2
a = [[3, 6, -4], [-12, 5, 7], [7, 9, -5]]
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
