# -*- coding: utf-8 -*-
# 回文字符串判断器
# 回文就是正读反读都一样的字符串，比如 "level"、"上海自来水来自海上"
# 新手练习：字符串操作、反转、循环

print("=" * 40)
print("     回文字符串判断器")
print("=" * 40)
print()
print("回文就是：正着读和倒着读完全一样的文字")
print("比如：level、12321、上海自来水来自海上")
print()

def shi_hui_wen(zi_fu_chuan):
    """判断一个字符串是不是回文，返回 True 或 False"""
    # 先预处理：转小写、去掉空格（让判断更灵活）
    s = zi_fu_chuan.lower()
    s = s.replace(" ", "")  # 去掉所有空格
    
    # 方法一：用反转字符串比较（Python 最方便的写法）
    fan_zhuan = s[::-1]  # 切片语法：[起始:结束:步长]，步长-1就是倒序
    if s == fan_zhuan:
        return True
    else:
        return False


def shi_hui_wen_shou_xie(zi_fu_chuan):
    """手写版：用循环从两端往中间比较（新手理解原理用）"""
    s = zi_fu_chuan.lower().replace(" ", "")
    changdu = len(s)
    
    # 从两头开始比，i 从左边，j 从右边
    i = 0
    j = changdu - 1
    
    while i < j:
        if s[i] != s[j]:
            return False  # 发现不一样，直接返回 False
        i = i + 1  # 左指针往右移
        j = j - 1  # 右指针往左移
    
    return True  # 循环完了都一样，就是回文


# 主循环
while True:
    wen_ben = input("请输入要判断的文字（输入 quit 退出）：")
    
    if wen_ben.lower() == "quit":
        print("再见！")
        break
    
    if wen_ben.strip() == "":
        print("你没有输入内容呢")
        print()
        continue
    
    # 用两种方法都判断一下，对比结果
    jieguo1 = shi_hui_wen(wen_ben)
    jieguo2 = shi_hui_wen_shou_xie(wen_ben)
    
    print()
    print(f"方法一（反转比较）：{'是回文 ✅' if jieguo1 else '不是回文 ❌'}")
    print(f"方法二（双指针对比）：{'是回文 ✅' if jieguo2 else '不是回文 ❌'}")
    
    if jieguo1:
        # 展示一下反转效果
        s = wen_ben.lower().replace(" ", "")
        print(f"原文：{wen_ben}")
        print(f"反转：{s[::-1]}")
    
    print()
