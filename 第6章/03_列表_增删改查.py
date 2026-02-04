# 新增操作
# 方式一：通过列表的append()方法，在列表尾部追加一个元素
nums = [10, 20, 30, 40]
nums.append(50)
print(nums)

# 方式二：通过列表的insert()方法，在列表的指定下标处添加一个元素
nums = [10, 20, 30, 40]
nums.insert(2, 50)
print(nums)

# 方式三：通过列表的extend()方法，将可迭代对象中的内容依次取出，追加到列表尾部
nums = [10, 20, 30, 40]
nums.extend('你好呀')
nums.extend(range(1, 4))
nums.extend([70, 80, 90])
print(nums)

# 删除操作
# 方式一：通过列表的pop()方法，删除指定位置的元素，并返回该元素
nums = [10, 20, 30, 40]
result = nums.pop(1)
print(nums)
print(result)

# 方式二：通过列表的remove()方法，删除列表中第一次出现的指定值
nums = [10, 20, 30, 40]
nums.remove(10)
print(nums)

# 方式三：通过列表的clear()方法，删除列表中所有元素（清空列表）
nums = [10, 20, 30, 40]
nums.clear()
print(nums)

