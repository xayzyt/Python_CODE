# reduce:对参数序列中元素进行累积
from functools import reduce
# reduce(funcation(a,b),sequence)   funcation必须有两个参数，sequence可迭代
li1 = [1,2,3,4]
def add(x, y):
    return x + y
res = reduce(add, li1)
print(res)      # 10


# 拆包：对于函数中的多个返回数据，去掉元组，列表或者字典 直接获取里面数据的过程
tua = (1,2,3,4)
print(tua)      # (1, 2, 3, 4)
a,b,c,d = tua
print(a,b,c,d)      # 1 2 3 4       把元素取出来

# 方法二
def funa (a,b,*args):
    print(a,b)
    print(args,type(args))
funa(1,2,3,4,5,6,7)
arg = (1,2,3,4,5,6,7)
funa(*arg)

# 异常
# 抛出异常
# raise

def funb ():
    # raise Exception("张云腾抛出异常")      # 执行了这句后面不运行
    print("哈哈哈哈哈")
    # raise Exception("张云腾抛出异常")
funb()


# 密码长度不足报错
def func():
    raise Exception("张云腾抛出异常")
def fund():
    print("密码正确")
def login():
    pwd = input("请输入密码")
    if len(pwd)>=6:
        fund()
    else:
        func()
# login()

# 捕获异常:代码不会终止
try:
    login()
except Exception as e:
    print(e)

# 模块
# 一个py文件就是一个模块
# 内置模块
# random time os logging 直接导入直接使用

# 第三方模块（第三方库）下载
# 下载：cmd窗口输入pip install 模块名

# 自定义模块
#自己在项目中定义模块

# 方法1   多使用这个
# improt +模块名
import pytest
print(pytest.name)
pytest.funa()       # 这是pytest模块中的funa（）
# 方法2
from pytest import funa ,name
funa()
print(name)
# 方法3
from pytest import *        # 所有内容导入
funa()
print(name)

# as 给模块起别名
import pytest as pt
pt.funa()
print(name)

# 给功能起别名
from pytest import funa as a
a()


# 内置全局变量
# 用来控制py文件在不同场景逻辑
import pytest1
pytest1.test1()




# 包:就是项目结构中的文件夹或目录
# 含有————init————.py模块（文件）

# 导入包时先执行————init————.py模块（文件）不建议在其写大量代码
from pack_01 import register    # 把这句放在————init————.py模块
register.reg()

# __all__:本质是列表，列表里面元素就代表导入模块
from pack_01 import *
login.log()


# 递归函数
# 在函数内部调用它本身
# 必须有一个结束条件
# 计算1-100累
def add1():
    s =0
    for i in range(1,101):
        s +=i
    print(s)

# 递归
def add2(n):
    if n==1:
        return 1
    return n + add2(n-1)
print(add2(5))


# 斐波那契数列
# 1,1,2,3,5,8,13
# 从第三项开始每一项为前两项和
def funf(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return funf(n-1)+funf(n-2)
print(funf(10))


# 闭包
# 函数嵌套定义：
# 1.在函数内部定义新函数
# 2.内层函数使用外层函数局部变量
# 3.外层函数的返回值是内层函数的函数名
def outer():
    n = 10
    def inner():
        print('inner',n)
    return inner
print(outer())

def outer1(m):
    n = 10
    def inner1(o):
        print('计算结果：',m+n+o)
    return inner1
ot = outer1(20)
ot(20)      # o =20 调用内函数


# 函数引用
# id（）判断两个变量是否是同一个值的引用
a = 1
print(a)
print(id(a))
a = 2
print(a)
print(id(a))        # 地址不同

# 装饰器
# 标准版装饰器
def send():
    print("发送消息")
def outer2(fn):
    def inner2():
        fn()
    return inner2
# print(outer2(send))    # 地址
ot1 = outer2(send)
ot1()


# 语法糖
# 格式：@装饰器名称
def outer3(fn):
    def inner3():
        print("登录")
        fn()
    return inner3
@outer3     # 不要加小括号
def send1():
    print("笑死了")
send1()

