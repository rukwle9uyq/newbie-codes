# -*- coding: utf-8 -*-
# 掷骰子模拟器
# 可以掷任意个骰子，统计点数
# 新手练习：random 模块、循环、统计

import random

print("=" * 30)
print("  🎲 掷骰子模拟器")
print("=" * 30)
print()

while True:
    # 问用户要掷几个骰子
    geshu = input("你想掷几个骰子(直接回车默认1个，输入q退出)：")
    
    if geshu.lower() == "q":
        print("游戏结束，拜拜！")
        break
    
    if geshu == "":
        geshu = 1
    else:
        # 判断是不是数字
        if not geshu.isdigit():
            print("请输入数字哦～")
            print()
            continue
        geshu = int(geshu)
        if geshu <= 0:
            print("骰子个数必须大于0")
            print()
            continue
    
    print()
    print(f"掷出 {geshu} 个骰子...")
    print("-" * 20)
    
    # 掷骰子
    dian_shu_list = []
    zongfen = 0  # 总分
    
    for i in range(geshu):
        # random.randint(a, b) 生成 a 到 b 之间的随机整数，包括两端
        dian = random.randint(1, 6)
        dian_shu_list.append(dian)
        zongfen = zongfen + dian
        
        # 打印每个骰子的结果
        print(f"  骰子 {i+1}: {dian} 点")
    
    print("-" * 20)
    print(f"  总点数: {zongfen}")
    print(f"  平均点数: {zongfen / geshu:.1f}")
    
    # 如果是多个骰子，看看有没有豹子（全一样）
    if geshu >= 2:
        quan_yiyang = True
        first = dian_shu_list[0]
        for d in dian_shu_list:
            if d != first:
                quan_yiyang = False
                break  # 发现不一样就不用再比了
        if quan_yiyang:
            print(f"  🎉 哇！豹子！全是 {first} 点！")
    
    print()
