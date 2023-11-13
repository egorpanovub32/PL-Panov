def F():
    max = 0
    while True:
        a = int(input())
        if a == 0:
            break
        if a > max:
            max = a
    return max
max = F()
print(max)