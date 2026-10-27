# -*- coding: utf-8 -*-
# 斐波那契数列生成器
# 斐波那契数列就是：1, 1, 2, 3, 5, 8, 13...
# 每个数等于前面两个数相加
# 新手练习：循环、列表、用户输入

print("=" * 35)
print("  斐波那契数列生成器")
print("=" * 35)
print()

# 获取用户想生成多少项
while True:
    n_str = input("你想生成几项斐波那契数？请输入数字：")
    
    # 判断输入是不是正整数
    if not n_str.isdigit():
        print("请输入正整数哦！")
        continue
    
    n = int(n_str)
    if n <= 0:
        print("项数必须大于0呢")
        continue
    break

# 用列表存结果
shulie = []

# 前面两项都是 1
if n >= 1:
    shulie.append(1)
if n >= 2:
    shulie.append(1)

# 从第3项开始，每一项 = 前两项之和
i = 2  # i 是当前要算的是第几个（从0开始数，所以第3个是索引2）
while i < n:
    xia_yi_ge = shulie[i-1] + shulie[i-2]
    shulie.append(xia_yi_ge)
    i = i + 1  # 新手写法，不用 += 也可以

# 打印结果
print()
print(f"前 {n} 项斐波那契数列是：")
print()

# 打印出来，每10个换一行，好看一点
count = 0
for shu in shulie:
    print(f"{shu:>8}", end=" ")  # 右对齐，占8个字符宽
    count = count + 1
    if count % 10 == 0:
        print()  # 换行

if count % 10 != 0:
    print()  # 最后补一个换行

print()
print(f"第 {n} 项的值是：{shulie[-1]}")
