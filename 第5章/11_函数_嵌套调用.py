# 嵌套调用：在一个函数的执行过程中，去调用了另外一个函数
def speak(msg):
    print('------------------')
    print(msg)
    print('------------------')


def greet(name, msg):
    print(f'我叫{name},我想说的话在下面：')
    speak(msg)
    print('嗯，我想说的结束了')


greet('张三', '你好啊')
