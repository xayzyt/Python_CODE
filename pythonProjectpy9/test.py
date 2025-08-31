# 模块的导入
# imoprt导入
import time         # time所有功能都能用
print("你好")
time.sleep(1)       # 间隔两秒
print("好")
# from导入
from time import sleep  # 只有sleep能用
# 直接写sleep就行
print("你好")
sleep(1)       # 间隔两秒
print("好")

# from time import *        全部导入，区别是下面使用功能时直接使用
from time import *
print("你好")
sleep(1)       # 间隔两秒
print("好")

# 导入包
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()

# 安装三方包
# pip install 包名    下载慢
# 国内下载
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名

