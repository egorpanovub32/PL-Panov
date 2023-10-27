#ВАРИАНТ 7


# №7
a = [1, 3, 4, 5, 2, 234, 53, 3453, 34, 23, 54, 2445]
summ = 0
umn = 1
for i in range(len(a)): #ищем четные элементы массива по индексу
    if i % 2 == 0:
        summ += a[i] #сумма четных элементов
    else:
        umn *= a[i] #произведение нечетных эелемнтов
print(summ, umn)

mas = [1, 3, 4, 6, 2, 24, 53, 245, 23, -134]
maxes = 0
minim = 0
for i in range(len(mas)):
    if mas[i] <= min(mas): #ищем индекс минимального числа
        minim = i
    elif mas[i] >= max(mas): #ищем индекс максимального числа
        maxes = i
mas[minim], mas[maxes] = mas[maxes], mas[minim] #меняем местами
print(mas)