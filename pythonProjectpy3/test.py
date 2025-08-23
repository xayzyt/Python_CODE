# 字符串编码转换
a = 'hello'
print(a,type(a))
a1 = a.encode()     # 编码
print(a1)
print(type(a1))
a2 = a1.decode()
print(a2)
print(type(a2))


st = 'hello word'
st1 = st.encode("utf-8")
print(st1,type(st1))
st2 = st1.decode("utf-8")
print(st2,type(st2))

# 字符串常见操作
# +字符串拼接
print("10"+ "10") # 拼接两个字符串

# *重复输出
print("好好学习\n"*5)  # 重复输出5次

# 成员运算符
# 检查字符串中是否包含了某个子字符串
# in ：包含返回True，不包含返回False
# not in ：包含返回True，不包含返回False
name3 = "zhanzgahng"
print('z' in name3)  # True
print('i' in name3)     # False
print('z' not in name3)     # False

# 下标
# 从左往右
print(name3[0])
print(name3[1])
print(name3[2])
print(name3[3])
print(name3[4])

# 从右往左数
print(name3[-1])
print(name3[-2])
print(name3[-3])
print(name3[-4])

# 切片
# 从操作对象截取一部分
# 包前不包后
name4 = 'abcdefg'
print(name4[0:5])   # abcde
print(name4[4:7])   # efg
print(name4[-5:])   # cdefg
print(name4[3:])    # defg
print(name4[-5:-1])     # cdef
print(name4[-1:-5]) # 空

# 查找
# find ：检测某个子字符串是否包含字符串中
print(name4.find('g'))  # 返回下标6
print(name4.find('bcd'))    # 返回b的下标
print(name4.find('z'))      # 找不到返回-1
print(name4.find('g',3,7))      # 包前不包后

# index：找不到报错与find的最大区别
print(name4.index('d'))     # 返回下标
# print(name4.index('z'))     # 报错

# count(): 返回子字符串在字符串出现次数，没有返回0
print(name4.count('z'))     #0
print(name4.count('g',3,7))     #包前不包后

# 判断
# startswith：判断是否以某个子字符串开头
# 返回 True False
print(name4.startswith('a'))    # True
print(name4.startswith('b'))    # Flase
print(name4.startswith('c',2,6))    # True

# endswith():是否以某个字符串结尾
print(name4.endswith('a'))      # False
print(name4.endswith('g'))      # True
print(name4.endswith('f',3,6))      # True

# isupper:检测字符串字母是否都为大写
print(name4.isupper())      # False

# 修改元素
# replace
name5 = "好好学习，天天向上"
print(name5.replace("天","时"))   # 都替换
print(name5.replace("天","时",1)) # 替换一次

# split（）：指定分隔符切字符
st1 = "hello,python"
print(st1.split(','))
print(st1.split('o'))   # ['hell', ',pyth', 'n']
print(st1.split('o',1)) # ['hell', ',python']

# capitalize():第一个字符大写,其他小写
st3 = "aBcd"
print(st3.capitalize())     # Abcd

# lower :大写字母转为小写
print(st3.lower())  # abcd

# upper：小写字母转大写
print(st3.upper())  # ABCD

# 列表
# 列表名 = [元素1，元素2，元素3]       数据类型可以不同
li = [1,2,3,4,a]
print(li,type(li))
print(li[2])

# append
li1 = ['one','two','three']
li1.append('four')
print(li1)      # ['one', 'two', 'three', 'four']

# extend    #分散添加
li2 = ['one','two','three']
li2.extend('four')
print(li2)      # ['one', 'two', 'three', 'f', 'o', 'u', 'r']


# insert    #指定位置插入元素，若有元素，那就会后移
li3 = ['one','two','three']
li3.insert(3,'four')
print(li3)

# 直接通过下标就可以修改
li5 = [1,2,3,4]
li5[1] = 'a'
print(li5)

# 查询
# 与字符串相同
# in    not in
li6 = [1,2,3,4]
print(2 in li6)

# 用户输入昵称，昵称重复不能使用
name_list = ["zhangyunteng","xiaozhang","xiaowang"]
while True:
    name = input("请输入昵称")
    if name in name_list:
        print(f"您输入的昵称{name}已经存在")
    else:
        print(f"您输入的昵称{name}已经创建")
        name_list.append(name)
        print(name_list)
        break
# index
# count
# 用法相同与上

# del
li7 = [1,2,3,4]
del li7[0]
print(li7)  # 删除了列表下标0的元素
# del li7   #整个删除

# pop：删除指定下标元素
li8 = [1,2,3,4]
li8.pop(2)
print(li8)

# remove ：根据元素的值删除
li9 = [1,2,3,4]
li9.remove(3)
print(li9)

# 排序
# sort：将列表按特定顺序从新排列
# 从小到大
li10 = [1,10,5,8]
li10.sort()
print(li10)

# reverse：颠倒，把后面的放到前面
li11 = [1,10,5,8]
li11.reverse()
print(li11)

# 列表推导式
li12 = []
[li12.append(i) for i in range(1,11)]
print(li12)

# 把奇数放进列表
li13 = []
[li13.append(j) for j in range(1,11) if j%2==1]
print(li13)


# 列表嵌套
# 一个列表里有另一个列表
li14 = [1,2,3,[4,5,6]]
print(li14[3])
print(li14[3][1])

# 元组

tua = (1,2,3,4,5)
tua1 = (1, 2, 3, 'a', 5)    #可以是不同数据类型
print(tua)
print(tua1)
print(type(tua))

# 元组只支持查询，不支持增加删除更改
print(tua[0])


# 字典
# 格式 ： 字典名 = {键1：值1，键2：值2...}
dic = {'name':'zhangyunteng','age':23}
print(type(dic))
print(dic)

# 字典常见操作
# 查看元素
# 变量名【键名】
dic1 = {'name':'zhangyunteng','age':23}
print(dic1['age'])
print(dic1.get('age'))
# print(dic1['tel'])  #报错
print(dic1.get('tel'))  # 返回None
print(dic1.get('tel','不存在'))    # 不存在

# 修改元素
dic1['age'] = 20
print(dic1)

# 新增
dic1['tel'] = 12356
print(dic1)

# 删除
# del
del dic1['tel']
print(dic1)

# clear
# 清空整个字典但保留字典
dic.clear()
print(dic)

# pop
dic1.pop('age')
print(dic1)

# len求长度
dic2 = {'name':'zhangyunteng','age':23}
print(len(dic2))    # 有两个键值对


# keys返回字典里包含的所有键名
dic3 = {'name':'zhangyunteng','age':23}
print(dic3.keys())
for i in dic3.keys():
    print(i)

# values 值
dic4 = {'name':'zhangyunteng','age':23}
print(dic4.values())
for i in dic4.values():
    print(i)

# items 返回字典所有键值对，以元组形式
for i in dic4.items():
    print(i)    # ('name', 'zhangyunteng')  ('age', 23)

# 字典应用场景
#  使用键值对存储一个物体相关信息


# 集合
# 集合名 = {元素1，元素2，元素3}
s1 = {1,2,3,4}
print(s1,type(s1))
# s1 = {}       定义空字典
# s1 = set()      # 定义空集合


# 集合具有无序性
s2 = {'a','b','c','d'}
print(s1)
print(s2)       # 数字有顺序，字符无顺序

# 集合具有唯一性，自动去重
s3 = {1,2,3,4,4,3,2,1,0}
print(s3)      # {0, 1, 2, 3, 4}

# 集合常见操作
# 添加
# add
s4 = {1,2,3,4,5}
s4.add(6)       # 一次只能添加一个元素
print(s4)

# update
s5 = {1,2,3,4,5}
s5.update('678')    # 只能是字符串
print(s5)

# 删除元素
# remove
s6 = {1,2,3,4,5}
s6.remove(3)
print(s6)

# pop
s7 = {1,2,3,4,5}
s8 = {'a','b','c','d'}
s7.pop()
s8.pop()
print(s7)       # 删除第一个元素
print(s8)       # 删除无序排列第一个元素

# discard   # 与remove区别是它里面没有值去删除不会报错
s9 = {1,2,3,4,5}
s9.discard(3)
print(s9)

# 交集 &      无交集返回set（）空
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a&b)

# 并集 |      重复不算
print(a|b)
