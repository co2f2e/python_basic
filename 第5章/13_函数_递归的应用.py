# 递归的应用举例：使用递归求一个数的阶乘

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
