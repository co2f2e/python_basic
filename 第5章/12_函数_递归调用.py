# 递归调用：是指函数自己调用自己的一种操作

# 使用递归打印n次你好啊（从大到小）
# 先打印后递归
def welcome1(n):
    print(f'你好啊{n}')
    if n > 1:
        welcome1(n - 1)


welcome1(5)

print('*******************************')


# 使用递归打印n次你好啊（从小到大）
# 先递归后打印
def welcome2(n):
    if n > 1:
        welcome2(n - 1)
    print(f'你好啊{n}')


welcome2(5)
