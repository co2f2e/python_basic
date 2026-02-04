# 下标（索引值）：例表中元素的位置编号
# 正索引：从左往右数，起始元素是0，随后是1，以此类推
# 负索引：从右往左数，起始元素是-1，随后是-2，以此类推

# 定义一个列表
nums = [10, 20, 30, 40, 50]

# 测试正索引
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

# 测试负索引
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[-5])

# 定义一个嵌套列表
nums2 = [10, 20, ['你好呀', 'Python'], 40, 50]
# 取出"Python"
print(nums2[2][1])
