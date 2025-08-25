print("这是pytest1作为模块会显示的内容")
def test1 ():
    print("哈哈1")
if __name__ == "__main__":  # 被当作模块导入时下面代码不会显示,不想给别人看到
    print("这是pytest1作为模块不会显示的内容")
