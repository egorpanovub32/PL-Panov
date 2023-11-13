import math
x = int(input())
n = int(input())
def F(x,n):
    result= math.pow(x,n) / math.factorial(n)
    return result
res = F(x,n)
print(res)