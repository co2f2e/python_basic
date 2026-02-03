# 使用str()将指定数据转换为字符串
result1 = str(18)
result2 = str(75.6)
result3 = str(1.8e3)
result4 = str(12_000)

print(type(result1), result1)
print(type(result2), result2)
print(type(result3), result3)
print(type(result4), result4)

# 使用int()将指定数据转换为整型
result5 = int(15.6)
result6 = int('79')
result7 = int(' 79 ')
result8 = int(48)

print(type(result5), result5)
print(type(result6), result6)
print(type(result7), result7)
print(type(result8), result8)
# 以下是错误示例
# int(' 7 9 ')
# int('你好')
# int('79个')

# 使用float()将指定数据转换为浮点型
result9 = float(18)
result10 = float('15.6')
result11 = float(' 5.7 ')
result12 = float(14.8)
result13 = float('48')
# 以下是错误示例
# float(' 5. 7 ')
# float('你好')
# float(' 5.7元 ')
# float('5.23.12')
print(type(result9), result9)
print(type(result10), result10)
print(type(result11), result11)
print(type(result12), result12)
print(type(result13), result13)
