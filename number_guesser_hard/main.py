# -*- coding: utf-8 -*-
# 进阶猜数字游戏
# 比入门版多了：难度选择、计分、历史记录
# 新手练习：函数、列表、多分支、随机数

import random
import math

print("=" * 45)
print("     🔢 进阶猜数字游戏")
print("=" * 45)
print()

# 历史记录：存每局的猜测次数
li_shi = []


def yi_ju_you_xi(fan_wei, ming_ci):
    """玩一局游戏，返回猜了几次
    fan_wei: 数字范围上限 (1到fan_wei)
    ming_ci: 最多可以猜几次
    """
    # 随机生成答案
    da_an = random.randint(1, fan_wei)
    print(f"我想了一个 1 到 {fan_wei} 之间的数字")
    print(f"你有 {ming_ci} 次机会")
    print()
    
    cishu = 0  # 猜了几次
    
    while cishu < ming_ci:
        cishu = cishu + 1
        
        # 获取输入
        yonghu_shuru = input(f"第 {cishu} 次，请猜：")
        
        # 判断是不是数字
        if not yonghu_shuru.isdigit():
            print("请输入数字哦！")
            cishu = cishu - 1  # 输入错误不算次数
            continue
        
        cai = int(yonghu_shuru)
        
        if cai < 1 or cai > fan_wei:
            print(f"数字在 1 到 {fan_wei} 之间！")
            cishu = cishu - 1
            continue
        
        # 判断大小
        if cai < da_an:
            print("太小啦！往上猜")
        elif cai > da_an:
            print("太大啦！往下猜")
        else:
            print(f"🎉 恭喜你，猜对了！用了 {cishu} 次")
            return cishu  # 猜对了，返回次数
        
        # 给点提示，还剩几次
        sheng_yu = ming_ci - cishu
        if sheng_yu > 0:
            print(f"还有 {sheng_yu} 次机会")
    
    # 循环结束了还没return，说明用完次数了
    print(f"😅 机会用完了，答案是 {da_an}")
    return 0  # 返回0表示没猜出来


# 主菜单循环
while True:
    print("请选择难度：")
    print("  1 - 简单 (1-50, 10次机会)")
    print("  2 - 普通 (1-100, 7次机会)")
    print("  3 - 困难 (1-500, 10次机会)")
    print("  4 - 查看历史记录")
    print("  5 - 退出")
    print()
    
    xuanze = input("请输入选项(1-5)：")
    
    if xuanze == "5":
        print("再见！欢迎再来玩～")
        break
    
    if xuanze == "4":
        # 显示历史记录
        print()
        print("-" * 30)
        print("       📜 历史记录")
        print("-" * 30)
        if len(li_shi) == 0:
            print("还没有记录呢，去玩一局吧！")
        else:
            sheng_li_de = [x for x in li_shi if x > 0]
            print(f"总局数：{len(li_shi)}")
            print(f"胜利局：{len(sheng_li_de)}")
            if len(sheng_li_de) > 0:
                pingjun = sum(sheng_li_de) / len(sheng_li_de)
                print(f"平均猜测次数：{pingjun:.1f}")
                print(f"最少次数：{min(sheng_li_de)}")
            print()
            for i, ci in enumerate(li_shi):
                zhuangtai = "胜" if ci > 0 else "负"
                ci_shu_str = str(ci) + "次" if ci > 0 else "-"
                print(f"  第{i+1}局: {zhuangtai}  {ci_shu_str}")
        print("-" * 30)
        print()
        continue
    
    # 设置难度参数
    if xuanze == "1":
        fan_wei = 50
        ming_ci = 10
    elif xuanze == "2":
        fan_wei = 100
        ming_ci = 7
    elif xuanze == "3":
        fan_wei = 500
        ming_ci = 10
    else:
        print("选项不对，请重新选")
        print()
        continue
    
    print()
    jie_guo = yi_ju_you_xi(fan_wei, ming_ci)
    li_shi.append(jie_guo)  # 记录到历史里
    print()

print()
print("程序退出了")
