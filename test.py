# 面向过程：每一步都要亲力亲为
# 面向对象：有人去做，找别人帮助做
# 类：就是一系列具有相同属性和行为的统称，不真实存在
# 对象：对象是类的具体实现，是类创建出真实存在的事物
# 类的三要素：类名，属性，方法
# 举例
# 类名：人类
# 属性：身高、体重、年龄
# 方法：走路、说话、思考

# 定义类
# class 类名：
#      代码块
# 洗衣机
class Washier:
    height = 800
    width = 800
# 查看属性
print(Washier.height)
print(Washier.width)
# 新增类属性
Washier.long = 800
print(Washier.long)
# 创建对象   一个类可以创建多个对象
wa = Washier()
print(wa)       # 对象在内存地址

class Washer:
    height = 800    # 类属性
    def wash(self): # self参数是类中实例方法必须具备
        print("我会洗衣")
# 实例化对象
wa1 =Washer()
wa1.wash()


# 实例化属性
class Person:
    name = "zhang"
    def introduce(self):    # 实例方法
        print("我是实例")
        print(f"{Person.name}的年龄：{self.name}")
pe = Person()
pe.age=18       # 实例属性
pe.sex="男"
pe.introduce()
# 实列属性只能由对象名访问

pe2 = Person()
pe2.sex="man"
print(pe2.sex)

# 每实例化一次就要添加一次属性所以可以用构造函数
# 构造函数  __init__()
# 通常用来属性初始化
# class Test:
#     def __init__(self):
#         print("这是init函数")
# te=Test()

# 构造函数用法    多使用构造函数
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def play(self) :
        print(f"{self.name}在玩")
    def introduce(self):
        print(f"{self.name}介绍{self.age}")
pe1 = Person("zhang",18)
pe1.play()
pe1.introduce()
pe2 = Person("wang",18)
pe2.play()
pe2.introduce()


# 析构函数
# 主要用在这个程序已经全部执行结束
# __del__意味对象不能继续引用
# 删除对象时，解释器会默认调用
# class Person1:
#     def __init__(self):
#         print("我是init") # 1
#     def __del__(self):
#         print("被销毁了")   # 2
# p2= Person1()
# print("zhedsakd")   # 3
# 正常运行不会调用del所以顺序是 1,3,2

class Person1:
    def __init__(self):
        print("我是init") # 1
    def __del__(self):
        print("被销毁了")   # 2
p2= Person1()
del p2
print("zhedsakd")   # 3
# 顺序为：1，2，3

# 封装
# 面向对象的三大特性：封装，继承，多态
# 封装：隐藏对象中不希望被外部所访问到的属性或方法
# class Person2:
#     name = "zhang"
# pe3=Person2()
# print(pe3.name)

# 隐藏属性：__
class Person2:
    name = "james"
    __age = 40  # 隐藏属性
pe3=Person2()
print(pe3.name)
# print(pe3.age)

# 访问隐藏属性
class Person3:
    name = "james"
    __age = 40  # 隐藏属性
pe4=Person3()
print(pe4.name)
print(pe4._Person3__age)    # 可以访问

# 方法二:正规方法
class Person4:
    name = "james"
    __age = 40  # 隐藏属性
    def measure2(self):
        print(f"{Person4.name}是{Person4.__age} ")
pe5=Person4()
print(pe5.name)
pe5.measure2()


# _xxx单下划线开头声明私有属性外部可以使用，子类可继承但不能导入

class Person5:
    name = "james"
    __age = 40  # 隐藏属性
    _sex = "man"
pe6=Person5()
print(pe6.name)
print(pe6._Person5__age)
# 使用对象名，——属性名调用
print(pe6._sex)

class Man:
    def __play(self):
        print("玩手机")
    def funk(self):
        print("sdad")
ma = Man()
ma.funk()
ma._Man__play()

# 私有方法
class Girl:
    def _buy(self):
        print("buybuybuy")
girl = Girl()
girl._buy()

# 继承
# 子类默认继承父类属性和方法
# calss 类名（父类）:
# 单继承
class Personw:
    def eat(self):
        print("吃饭")
    def sing(self):
        print("唱歌")
class Girl1(Personw):       # 继承
    None   # 跳过
girl1 = Girl1()
girl1.eat()
girl1.sing()

# 继承传递:实际就是孙子类
class Father:
    def eat(self):
        print("吃饭")
    def sleep(self):
        print("睡觉")
class Son(Father):
    pass
son = Son()
son.eat()
son.sleep()
class Grandson(Son):
    pass
grandson = Grandson()
grandson.eat()
grandson.sleep()

# 方法重写
# 子类重写父类
# 在子类中定义与父类相同名称的方法

class Father1:
    def eat(self):
        print("吃饭")
    def sleep(self):
        print("睡觉")
class Son1(Father1):
    def eat(self):
        print("多吃")
    def sleep(self):
        # 即继承父类也覆盖父类的两种方法
        Father1.sleep(self)     # 第一种方法：睡觉
        super().sleep()         # 第二种方法：睡觉
        print("多睡")
son = Son1()
son.eat()
son.sleep()


# 新式类
# class A:        # 经典类：不由内置类型派生出的类
# class A(object):      新式类

# 多继承
class Father3(object):
    def eat(self):
        print("sajdka")
class Mother3(object):
    def money(self):
        print("hasdj")
class Son3(Father3,Mother3):
    pass
son3= Son3()
son3.eat()
son3.money()

# 多态
# 同一种行为具有多种表现形式
class Animal(object):
    def shout(self):
        print("动物会叫")
class Dog(Animal):
    def shout(self):
        print("wawawa")
class Cat(Animal):
    def shout(self):
        print("maimaiomaio")
# 多态
cat = Cat()
cat.shout()
dog = Dog()
dog.shout()

# 多态性
class Animal1(object):
    def eat(self):
        print("eat")
class Pig(Animal1):
    def eat(self):
        print("ahsdf")
class Dog1(Animal1):
    def eat(self):
        print("fhabf")
# 多态性
def test2(obj):
    obj.eat()
animal1 = Animal1()
pig = Pig()
test2(animal1)
test2(pig)


# 静态方法
# @staticmethod
class Person8(object):
    @staticmethod
    def study(nam):
        print(f"{nam}study")
Person8.study("zhang")
pe8 = Person8
pe8.study("zhang")
