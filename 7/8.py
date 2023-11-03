#Задание 8
#Найти все натуральные числа, не превосходящие заданного n, которые делятся на каждую из своих цифр.
def func1(i):
    a = i
    while(a):
        b = a % 10
        a //= 10
        if (b == 0 or i % b): #проверка на наличие нуля(т.к. на ноль делить нельзя) и на остаток от деления на свою цифру
            return False
    return True
n = int(input("Введите число: "))
for i in range(1, n + 1):
    if (func1(i)):
        print(i)

#Ввести одномерный массив A длиной m. Поменять в нём местами первый и последний элементы. Длину массива и его элементы ввести с клавиатуры. В программе описать процедуру для замены элементов массива. Вывести исходные и полученные массивы.
def func2(A):
    A[0], A[-1] = A[-1], A[0] #Функция, менящая местами первый и последний элемент
    return A

x = int(input("m = ")) #Длина массива
A = list(map(int, input("Введите элементы массива: ").split(maxsplit = x))) #Количество элементов вводится через пробел
print(A) #Вывод исходного массива
print(func2(A)) #Вывод изменённого массива