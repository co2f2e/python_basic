# 字符串的下标
msg = 'welcome to atguigu'
print(msg[3])
print(msg[-1])

# 字符串中的字符，不可修改
# msg='welcome to atguigu'
# msg[0]='a'

# 字符串不能嵌套
# 备注：符串中不能直接使用相同类型的引号进行嵌套；如果需要包含相同引号，应使用转义字符，或改用不同类型的引号作为字符串边界
# msg='welcome to'hello' atguigu'
# msg = 'welcome to"hello" atguigu'
# msg = 'welcome to\'hello\' atguigu'

# 常用方法
# index方法：获取指定字符，在字符串中第一次出现的下标
msg = '尚硅谷@atguigu@你好'
result = msg.split('@')
print(msg)
print(result)

# replace方法：将字符串中的某个字符片段，替换成目标字符串（不修改原字符串，返回新字符串）
msg = 'welcome to atguigu'
result = msg.replace('g', 'GG')
print(msg)
print(result)

# count方法：统计指定字符，在字符串中出现的次数
msg = 'welcome to atguigu'
result = msg.count('g')
print(result)

# strip方法：从某个字符串中删除指定字符串中的任意字符
# 规则：从字符串两端开始删除，直到遇到第一个不在指定字符串中的字符就停下
msg = '666尚6硅6谷666'
result = msg.strip('6')
print(result) # 尚6硅5谷
print(msg) # 666尚6硅6谷666

msg = '1234尚12硅34谷4321'
result = msg.strip('1324')
print(result) # 尚12硅34谷
print(msg) # 1234尚12硅34谷4321
