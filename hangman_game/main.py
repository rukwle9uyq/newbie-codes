# -*- coding: utf-8 -*-
# Hangman 猜单词游戏
# 电脑随机选一个单词，玩家一个个字母猜
# 猜错太多次就被"吊死"了
# 新手练习：随机、字符串、列表、循环

import random

print("=" * 40)
print("   🎮 Hangman 猜单词游戏")
print("=" * 40)
print()

# 单词库（都是简单的英文单词）
dan_ci_ku = [
    "python", "apple", "banana", "orange", "computer",
    "school", "student", "teacher", "happy", "sunny",
    "water", "flower", "friend", "family", "music",
    "pencil", "rabbit", "monkey", "guitar", "pizza",
]

# 随机选一个单词
zheng_que = random.choice(dan_ci_ku)
changdu = len(zheng_que)

# 记录玩家猜对的字母，初始全是下划线
yi_cai = ["_"] * changdu

# 记录猜错的字母
cuo_wu = []

# 最多可以错几次
zui_da_cuo_wu = 6
sheng_yu = zui_da_cuo_wu  # 剩余机会

# 游戏主循环
while True:
    # 显示当前状态
    print()
    print("单词：" + " ".join(yi_cai))
    print(f"剩余机会：{sheng_yu} 次")
    if len(cuo_wu) > 0:
        print(f"猜错的字母：{', '.join(cuo_wu)}")
    print()
    
    # 检查是不是已经猜完了（没有下划线了）
    if "_" not in yi_cai:
        print("🎉 恭喜你！猜对啦！")
        print(f"答案就是：{zheng_que}")
        break
    
    # 检查是不是已经用完机会了
    if sheng_yu <= 0:
        print("💀 啊哦，机会用完了...")
        print(f"正确答案是：{zheng_que}")
        print("下次加油！")
        break
    
    # 让玩家猜一个字母
    zi_mu = input("请猜一个字母：").lower().strip()
    
    # 验证输入
    if len(zi_mu) != 1:
        print("只能输入一个字母哦！")
        continue
    if not zi_mu.isalpha():
        print("请输入英文字母！")
        continue
    
    # 看看是不是已经猜过了
    if zi_mu in yi_cai or zi_mu in cuo_wu:
        print("这个字母你已经猜过了，换一个吧")
        continue
    
    # 判断对不对
    if zi_mu in zheng_que:
        # 猜对了！把所有这个字母的位置都填上
        print("✅ 猜对了！")
        # 遍历每个位置，如果是这个字母就替换下划线
        for i in range(changdu):
            if zheng_que[i] == zi_mu:
                yi_cai[i] = zi_mu
    else:
        # 猜错了
        print("❌ 猜错了...")
        cuo_wu.append(zi_mu)
        sheng_yu = sheng_yu - 1

print()
print("游戏结束")
