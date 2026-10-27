# -*- coding: utf-8 -*-
# 九九乘法表生成器
# 打印出完整的九九乘法表
# 新手练习：双重循环、字符串格式化

print("=" * 50)
print("           九九乘法表")
print("=" * 50)
print()

# 外层循环：第一个乘数，从 1 到 9
i = 1
while i <= 9:
    # 内层循环：第二个乘数，从 1 到 i（这样是三角形的）
    j = 1
    while j <= i:
        # 计算乘积
        cheng_ji = i * j
        # 打印，用 end="" 不换行，让一行里的算式并排
        # %2d 表示占两个字符宽度，右对齐，这样列对齐好看
        print(f"{j}×{i}={cheng_ji:<2}", end="  ")
        j = j + 1
    # 一行打完了，换行
    print()
    i = i + 1

print()
print("-" * 50)
print()

# 再打印一个完整方阵版本（9x9）
print("完整方阵版：")
print()

# 用 for 循环写一个版本，对比一下
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{result:>3}", end=" ")
    print()  # 换行

print()
print("搞定！九九乘法表打印完成～")
