# 备注：所有的列表方法，都只作用于当前层的元素（浅层操作），不会自动进入嵌套的里层结构中
# 1.使用index方法，查找指定元素在列表中第一次出现的下标，返回值是：元素下标
fruits = ['香蕉', '苹果', '橙子', '香蕉']
result = fruits.index('香蕉')
print(result)

# 2.使用count方法，统计某个元素在列表中出现的次数，返回值是：元素出现的次数
fruits = ['香蕉', '苹果', '橙子', '香蕉']
result = fruits.count('香蕉')
print(result)

# 3.使用reverse方法，对列表进行反转（会改变原列表）
nums = [23, 11, 32, 30, 17, [6, 7, 8, 9]]
nums.reverse()
print(nums)

# 4.使用sort方法，对列表排序（默认从小到大），若想从大到小，可以将reverse参数设为True
# 4.1若列表中的元素：都是数字，则按照数字的大小顺序进行排序
nums = [23, 11, 32, 30, 17]
nums.sort(reverse=True)
print(nums)

# 4.2若列表中的元素：既有数字，又有字符串，那就会报错
nums = [23, 11, 32, 30, 17, '你好啊']
# nums.sort()

# 4.3若列表中的元素：都是字符串，则按照字符串的Unicode编码大小进行排序
msg_list = ['北京', '尚硅谷', '你好']
msg_list.sort()
print(msg_list)
