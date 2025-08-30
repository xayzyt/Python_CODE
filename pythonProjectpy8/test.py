# 如果函数要返回多个返回值
def test_return ():
    return 1,2
x,y = test_return()
print(x,y)

# 不定长参数
# 位置传递：*args
def user_info(*args):           # 作为元组存在，并接受
    print(args)
user_info(1,2,3,"Tom")
# 关键字传递：**kwargs
def user_in(**kwargs):           # 作为字典存在，并接收
    print(kwargs)
user_in(name="Tom",age=20,tel = "12345")

# 函数作为参数传递
def compute(arg1,arg2):
    return arg1+arg2
def tset_func(compute):
    result = compute(1,2)
    print(result)
tset_func(compute)
# 匿名函数lambda    lambda只能写一行,只能用一次
tset_func(lambda x,y:x*y)


# 文件编码
# 将文件内容翻译成二进制
# 只用UTF—8


# 文件的读取操作
# 打开文件
# open(name,mode（三种模式：“r” “w” “a”）,encoding)
f = open(r"D:\test\测试.txt","r", encoding="UTF-8")
print(type(f))
# 读取文件
# print(f.read(10))          # 读取十个字节
# print(f.read())            # 读取全部内容(注意接上面read开始读取)
# print(f.readlines())       # 读取全部行封装到列表
# print(f.readline())          # 一次读取一行
# print(f.readline())          # 再读取一行

# for循环读取文件行
for line in f:
    print(line)

# 必须关闭文件 f.close()
f.close()

# 文件写操作
f = open(r"D:\test\测试.txt","w", encoding="UTF-8")
# 写入
f.write("hello world")
# 刷新
f.flush()
# 关闭
f.close()

# 异常
# 捕获异常
try:            # 可能出现异常，如果异常执行下面
    f = open("D:/abc.txt","r", encoding="UTF-8")
except:
    f = open("D:/abc.txt","w", encoding="UTF-8")
# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现变量未定义")
    print(e)            # name 'name' is not defined    记录异常

# 捕获全部异常
try:
    1/0
except Exception as e:
    print("异常")
    print(e)
else:
    print("else可选，没有异常时执行")
finally:
    print("finally可选，无论如何都会执行")
# 异常具有传递性
def func01():
    num = 1/0
    print(num)
def func02():
    func01()
def main():
    try:
        func02()
    except Exception as e:
        print(e)
main()

