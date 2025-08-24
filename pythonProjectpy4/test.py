# 类型转换
# 1.int:转换为一个整数，只能转换由纯数字组成的字符串
a = 1.2
print(type(a))      # <class 'float'>
b = int(a)
print(type(b))      # <class 'int'>
print(int(1.8))     # 1     不遵循四舍五入
# str->int
c = int('123')
print(c,type(c))    # 123 <class 'int'>
# 输入年龄判断成年
age = int(input('请输入年龄：'))

if age >= 18:
    print("您成年了")
else:
    print("您未成年")

# 2.float：转换为小数
print(float(11))


# 3.str字符串类型
n1 =100
print(type(n1))
n2 = str(n1)
print(type(n2))
print(n2)


# 4.eval：将字符串中的运算算出来返回整型    可以实现list dict tuple 和str的转换
print(10+10)
print('10'+'10')
print('10+10')
print(eval('10+10'))
print(type(eval('10+10')))      # <class 'int'>

# str->list
st1 = "[[1,2],[3,4],[5,6]]"
print(type(st1))
li = eval(st1)
print(li,type(li))

# str->dict
st2 = "{'name':'zhang','age':18}"
print(type(st2))
dic = eval(st2)
print(type(dic))
print(dic)

# eval非常强大但是不够安全



# 5.list（）将可迭代对象转换为列表
# 可迭代对象：str tuple dict set
# str->list
print(list('abcdef'))
# tuple ->list
print(list((1,2,3,4)))
# dict->list
print(list({'name':'zhang','age':18}))      # ['name', 'age']
# 字典转换成列表会取键名作为列表的值
# set->list
print(list({'a', 'b', 'c', 'a'}))
# 集合转换成列表先去重再转换


# 赋值
li1 = [1,2,3,4]
print(li1)
li2 = li1
print(li2)
# 一个值改变会被另一个值共享
li1.append(5)
print(li1)
print(li2)
# 地址相同
print("li1内存地址：",id(li1))
print("li2内存地址：",id(li2))

# 深浅拷贝
# 浅拷贝：
# 拷贝速度快，占用空间小，拷贝效率高
import copy     # 导入copy模块
li3 = [1,2,3,4,[5,6,7]]
li4 = copy.copy(li3)
print(li4)
# 地址不同
print("li3内存地址：",id(li3))
print("li4内存地址：",id(li4))
# 往嵌套列表添加元素,嵌套的列表会共享值
li3[4].append(8)
print(li3)
print(li4)
# 嵌套列表地址相同
print("li3[4]内存地址：",id(li3[4]))
print("li4[4]内存地址：",id(li4[4]))

# 深拷贝，数据完全不共享
# 外层和内层都copy
li5 = [1,2,3,4,[5,6,7]]
li6 = copy.deepcopy(li5)
print(li5)
print(li6)
# 查看地址
print("li5内存地址：",id(li5))
print("li6内存地址：",id(li6))

# 在嵌套列表添加,只有li5添加了
li5[4].append(8)
print(li5)
print(li6)
# 嵌套列表地址相同
print("li5[4]内存地址：",id(li5[4]))
print("li6[4]内存地址：",id(li6[4]))

# 可变对象:其中值可以变，地址不变
# 常见可变类型：list dict set，元组不行
li7 = [1,2,3,4]
print("li7原内存地址:", id(li7))
li7.append(5)
print(li7)
print("li7现内存地址:", id(li7))
# set
set1 = {1,2,3,4}
print(set1,id(set1))
set1.remove(3)
print(set1,id(set1))

# 不可变类型:变量对应的值不能被修改，如果修改就会从新分配空间
# 数值类型：int bool float complex   字符串         元组tuple
n = 10                 # int
print("源地址",id(n))
n = 15
print("现地址",id(n))

# str   地址改变
st = "hello"
print(st,id(st))
st = "zhang"
print(st,id(st))

# tuple
tua = (1,2,3)
print(tua,id(tua))
tua = ('1','b','c')
print(tua,id(tua))


# 函数
# 编写打招呼函数
def say_hello():
    print("hello")
# 调用函数
say_hello()
# 返回值，函数返回结果
def buy():
    return "ahaha"
buy()
print(buy())

# 函数遇到return不继续执行
def buy():
    return "ahaha",20       # 多值的情况返回元组形式
    # return 20
buy()
print(buy())

# 参数
def add (a,b):      # 形参
    return a+b

print(add(5,6))     # 实参

# 必备参数：传递和定义参数的顺序及个数必须一致
def funa(name1,name2,name3,name4):
    print(name1,name2,name3,name4)
# 写几个传几个
funa('z','x','g','u')

# 默认参数:为参数提供默认值，调用时可以不传递默认参数值
def funb(a = 8):
    print(a)
funb()
funb(354)
# 可变参数:传入值的数量可以改变，可以传入多个，也可以不传
def func(*args):
    print(args)
func(1,2,3)     # 以元组形式接受,传值要采用键值形式，可以拓展函数功能

# 关键字参数 # 区别以字典接受
def fund(**kwargs):
    print(kwargs)
fund()  # 空字典
fund(name='zhang',age=18)

# 函数嵌套
# def study():
#     print("晚上在学习")
# def course():
#     study()
#     print("python基础")
def study():
    print("晚上在学习")
    def course():
        print("python基础")
    course()    # 注意定义和调用是同级，调用在定义里面永远调用不到
study()

# 作用域
# 全局变量：函数外部定义变量
# 局部变量：函数内部定义变量
a =100
def test():
    print(a)
def test2():
    a = 120  # 局部变量
    print(a)
test2()
print(a)    # 全局变量

# 在函数内部修改全局变量用global
# global:将变量变为全局变量
a =100
def test3():
    print(a)
def test4():
    global a
    a = 120  # 全局变量
    print(a)
test4()
print(a)    # 全局变量

# 匿名函数
# lambda
add = lambda a,b:a+b
print(add(10,20))

# 无参数
funh = lambda:"dads"
print(funh())
# 一个参数
funl = lambda name:name
print(funl("zhang"))
# 默认参数
funk = lambda name,age:(name,age)
print(funk("zhang",18))
# 关键字参数
funj = lambda **kwargs:kwargs
print(funj(name="zhang",age=18))


# lambda结合if判断
j = 5
k = 8
print("j比k小")if j<k else print("j大于等于k")
comp = lambda j,k:"j比k小"if a<b else "a大于等于b"
print(comp(8,5))

# 内置函数
# 查看所有内置函数
import builtins
print(dir(builtins))    # 大写开头内置常量小写内置函数
# abs:返回绝对值
print(abs(-10))
# sum：返回和
print(sum((1,2)))
# min():求最小值    max求最大值
print(min(3,4,6))
print(max(3,4,6))

# zip:打包成元组
li11 = [1,2,3,4]
li12 = ["a","b","c"]
print(zip(li11,li12))
for i in zip(li11,li12):
    print(i)


# map：可以对对像中每一个元素映射
li13 = [1,2,3,4]
def funz(x):
    return x*5
mp = map(funz,li13)
print(mp)
for i in mp:
    print(i)