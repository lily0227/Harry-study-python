#过山车游戏
'''
软件要求：
身高1.4米 且年龄超过10 岁的人才可以坐过山车
'''
age= int(input("请输入您的年龄："))
height=float(input("请输入您的身高："))

if age>8 and height >1.4:
    print("恭喜您，可以参与过山车游戏")
else:
    print("不好意思，您的身高或者年龄不满足需求")
    