# -*- coding: utf-8 -*-
# 词频统计小程序
# 输入一段英文文字，统计每个单词出现的次数
# 新手练习：字典、字符串分割、排序

import string

print("=" * 45)
print("         词频统计小工具")
print("=" * 45)
print()
print("请输入一段英文文本（输入空行结束）：")
print()

# 读取多行输入，直到遇到空行
hang_list = []
while True:
    hang = input()
    if hang == "":
        break
    hang_list.append(hang)

# 把所有行拼成一个大字符串
wen_ben = " ".join(hang_list)

if len(wen_ben.strip()) == 0:
    print("你没有输入任何内容呢")
    exit()

print()
print("正在统计...")
print()

# 转成全小写，这样 "Hello" 和 "hello" 算同一个
wen_ben = wen_ben.lower()

# 去掉标点符号（新手写法：一个个替换）
for biaodian in string.punctuation:
    wen_ben = wen_ben.replace(biaodian, " ")

# 按空格分割成单词列表
words = wen_ben.split()

# 用字典存统计结果：键是单词，值是次数
cishu = {}

for dan_ci in words:
    # 跳过空字符串
    if dan_ci == "":
        continue
    # 如果字典里已经有这个单词，次数+1；没有就设为1
    if dan_ci in cishu:
        cishu[dan_ci] = cishu[dan_ci] + 1
    else:
        cishu[dan_ci] = 1

# 按次数从多到少排序
# sorted 的 key 参数指定按什么排序，reverse=True 降序
sorted_words = sorted(cishu.items(), key=lambda x: x[1], reverse=True)

# 打印结果
total_words = len(words)
diff_words = len(cishu)

print(f"总单词数：{total_words}")
print(f"不同单词数：{diff_words}")
print()

print("-" * 35)
print(f"{'排名':<6}{'单词':<15}{'次数':<8}{'占比':<8}")
print("-" * 35)

# 只显示前20个，太多了屏幕放不下
paiming = 1
for word, cnt in sorted_words[:20]:
    zhanbi = cnt / total_words * 100
    print(f"{paiming:<6}{word:<15}{cnt:<8}{zhanbi:.1f}%")
    paiming = paiming + 1

if len(sorted_words) > 20:
    print(f"... 还有 {len(sorted_words) - 20} 个单词没显示")

print("-" * 35)
print()
print("统计完成！")
