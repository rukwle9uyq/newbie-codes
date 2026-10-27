# -*- coding: utf-8 -*-
# 温度转换小程序
# 可以把摄氏度转成华氏度，也可以反过来
# 新手练习：学习用户输入、函数、条件判断

print("=" * 30)
print("  欢迎使用温度转换小工具")
print("=" * 30)
print()

# 定义转换函数，摄氏转华氏
def sheshi_huashi(c):
    # 公式：F = C * 9/5 + 32
    f = c * 9 / 5 + 32
    return f

# 华氏转摄氏
def huashi_sheshi(f):
    # 公式：C = (F - 32) * 5/9
    c = (f - 32) * 5 / 9
    return c

# 主循环，让用户可以多次转换
while True:
    print("请选择转换类型：")
    print("  1 - 摄氏度 -> 华氏度")
    print("  2 - 华氏度 -> 摄氏度")
    print("  3 - 退出程序")
    
    xuanze = input("请输入选项(1/2/3)：")
    
    if xuanze == "3":
        print("再见啦！")
        break  # 退出循环
    
    if xuanze not in ["1", "2"]:
        print("输入不对哦，请重新选择")
        print()
        continue  # 跳过后面，重新开始
    
    # 让用户输入温度数值
    try:
        wendu = float(input("请输入温度数值："))
    except ValueError:
        print("哎呀，你输入的不是数字呢，请重新来")
        print()
        continue
    
    # 根据选择进行转换
    if xuanze == "1":
        jieguo = sheshi_huashi(wendu)
        print(f"{wendu} 摄氏度 = {jieguo:.2f} 华氏度")
    else:
        jieguo = huashi_sheshi(wendu)
        print(f"{wendu} 华氏度 = {jieguo:.2f} 摄氏度")
    
    print()  # 空一行，好看一点
