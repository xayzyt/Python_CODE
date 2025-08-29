# 设计一个类
class Stduent:
    name = None
    gender = None
    age = None
# 创建一个对象
stu_1 = Stduent()
# 对象属性赋值
stu_1.name = "张云腾"
stu_1.gender = "M"
stu_1.age = 18
# 获取对象中记录的信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.age)


class Student1:
    name = None
    age = None
    def say_hi(self):
        print(f"Hello!!!,我是{self.name}")
    def say_hello(self,msg):
        print(f"Hello,我是{self.name},{msg}")

stu1 = Student1()
stu1.name = "张云腾"
stu1.say_hi()
stu1.age = 18


stu2 = Student1()
stu2.name = "James"
stu2.say_hello("King")
stu2.age = 40


# 设计一个闹钟
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
# 构建两个闹钟对象
clock1 = Clock()
clock1.id = 123454
clock1.price = 100
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
# clock1.ring()

clock2 = Clock()
clock2.id = 123455
clock2.price = 101
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
# clock2.ring()

# 构造方法:高效方法     __init__
class Student2:
    name = None
    age = None
    tel = None
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print(f"建立对象Hello!!!,我是{self.name}")
stu3 = Student2("周杰伦",31,"123535")
print(stu3.name)
print(stu3.age)
print(stu3.tel)

# 类内置方法
# 魔术方法:__init__  __str__  __lt__  __le__  __eq__
# __str__字符串方法
class Student3:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
# stu4 = Student3("ashjkdkji",5)
# print(stu4)
# print(str(stu4))
# 使用魔术
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
stu4 = Student3("wang",32)
print(stu4)
print(str(stu4))


# __lt__ 小于符号比较方法
class Student5:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __lt__(self, other):
        return self.age < other.age
stu5 = Student5("wang",32)
stu6 = Student5("zhang",23)
print(stu6 < stu5)

# __le__ 判断小于等于和大于等于
class Student6:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __le__(self, other):
        return self.age <= other.age
stu7 = Student6("wang",32)
stu8 = Student6("zhang",32)
print(stu7 <= stu8)

# __eq__ 比较运算符实现方法:判断是不是相等
class Student7:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
stu9 = Student7("wang",32)
stu10 = Student7("zhang",32)
print(stu9 == stu10)

# 封装
class Phone:
    IMEI = None
    producer = None
    __current_voltage = 0.5
    def __keep__single_core(self):
        print("让cpu单核运行")
    def call_by_5G(self):
        if self.__current_voltage >=1:  # 内部可以使用
            print("5G开启")
        else:
            self.__keep__single_core()
            print("电量不足，已经设置单核省电运行")
phone = Phone()
phone.IMEI = "123456"
phone.producer = "海思"
# print(phone.__current_voltage)  # 没办法直接使用
phone.call_by_5G()

# 继承
# 单继承 class 类名（父类）
class iPhone4:
    IMEI = None
    producer = "APPLE"
    def call_by_4G(self):
        print("4G通话")
class iPhone5(iPhone4): # 继承
    face_id ="10001"
    def call_by_5G(self):
        print("5G通话")
phone5 = iPhone5()
print(phone5.IMEI)
print(phone5.producer)
print(phone5.face_id)
phone5.call_by_5G()




# 多继承:继承多个父类
class xiaomi_1:
    IMEI = None
    producer = "xiaomi"
    def call_by_4G(self):
        print("4G通话")
class NFCReader:
    nfc_type = 5
    producer = "honer"
    def read(self):
        print("NFC读卡")
    def write(self):
        print("NFC写卡")
class RomoteController:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启")
class xiaomi_2(xiaomi_1,NFCReader, RomoteController):
    pass

xiaomik80 = xiaomi_2()
xiaomik80.call_by_4G()
xiaomik80.control()
xiaomik80.read()
xiaomik80.write()
print(xiaomik80.producer)

# 复写和使用父类成员
class OPPO:
    IMEI = None
    producer = "OPPO"
    def call_by_5G(self):
        print("父类的5G通话")
class MyOPPO(OPPO):
    IMEI = "1235331"
    producer = "高通"
    def call_by_5G(self):
        print("子类的5G通话")
        # 调用父类方法
        # 方法一：OPPO.call_by_5G(self)       # 注意加self
        #       print(OPPO.IMEI)
        # 方法二：
        super().call_by_5G()
        print(super().producer)
oppo = MyOPPO()
oppo.call_by_5G()
print(oppo.IMEI)
print(oppo.producer)


# 多态
# 抽象与多态结合
class Animal:
    def speak(self):
        pass                # 抽象：用作顶层设计
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
dog = Dog()
# dog.speak()
cat = Cat()
# cat.speak()
def make_sound(animal:Animal):
    animal.speak()
make_sound(dog)
make_sound(cat)

