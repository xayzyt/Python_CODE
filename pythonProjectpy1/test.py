# 1.python是面向对象的解释型高级编程语言
# 2.python是强类型的动态脚本语言
print("hello world")

# 设置断点
print(123)
print(123)
print(123)
print(123)
print(123)
print(123)
print(123)
print(123)

# 多个值用逗号隔开
# sep可以间隔多个值
print("hahaha","hehiehei","heheh",sep='|')
# end 用来设定以什么结尾
print("hello",end='world')
print("python")


# 1.变量的作用
# 计算机中存储空间，用来保存数据
# 2.定义变量的格式
# 变量名 = 值
num1 = 3    # num1是一个变量
num2 = 4    # num2是一个变量
print(num1+num2)

# 数值类型
# 1.int 2.float（浮点型） 3.bool（布尔型） 4. complx（复数）

# 检测数据类型的方法（type）
# 1.
num = 1
print(type(num))

# 2. float
num3 = 1.2
print(type(num3))

# 3.bool 通常用于判断
print(type(True))   # 相当于整数1
print(type(False))

# 4.complex
# 固定写法 z = a+bj
ma = 1 + 2j
mu = 2+ 3j

print (ma+mu)

# 格式化输出
# 占位符
# 1.% 2.
name = "zhang"
print("我是%s" %name)

# 2.%d
age = 18
name = "zhang"
print("我的名字：%s,年龄: %d "%(name,age))

# 3.%f
v = 1.2
print("%f"%v)

# 4.%.8f   要加.
b = 2.34567
print("%.8f"%b)

# 5. %%
print("woshi%%de"%())

# 6.f格式化
name5 = "zhangyunteng"
age = 18
print(f"{name5},wo {age}")


# // 向下取整，只要有小数就忽略小数部分
k = 5
j = 2
print(k//j)

# %取余数
print(k%j)

# ** 取幂
print(k**j) # 5的二次方

# 输入函数 input（）
# input(prompt) # prompt是提示，在控制台显示
fack = input("请输入：")

# \t 缩进
print("six\taar")

# \n 换行
print("haha\n")

# \r 回车 将后面的移动到开头
print("sixad\rdasd")

# \\
print("sis\\tdfsa")


# if判断

age2 = 17
if age2 <18:
    print("未成年")

score = input("输出成绩")
if score=='100':
    print("你真棒")
if score=='60':
    print("继续加油")

#  逻辑运算符
# and
o = "hah"
l = "hehe"
if o=="hah"and l=="hehe":
    print("a and b")

# or 或者
# not 表示相反的结果


# if - else
# if - elif
# if - elif - else



