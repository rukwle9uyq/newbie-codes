# -*- coding: utf-8 -*-
# 简易待办清单
# 可以添加、查看、完成、删除待办事项
# 新手练习：列表操作、函数封装、文件读写

import os

print("=" * 45)
print("        📝 简易待办清单")
print("=" * 45)

# 数据文件路径，把待办存在本地文件里
wen_jian_ming = "todo.txt"

# 待办列表，每个元素是一个字典：{内容, 是否完成}
todo_list = []


def jia_zai_shu_ju():
    """从文件加载待办数据"""
    if not os.path.exists(wen_jian_ming):
        return  # 文件不存在就不用加载了
    
    try:
        f = open(wen_jian_ming, "r", encoding="utf-8")
        hang = f.readline()
        while hang:
            hang = hang.strip()
            if hang == "":
                hang = f.readline()
                continue
            # 每行格式：0|内容  或者  1|内容  （0表示未完成，1表示已完成）
            parts = hang.split("|", 1)
            if len(parts) == 2:
                yi_wan_cheng = (parts[0] == "1")
                nei_rong = parts[1]
                todo_list.append({"内容": nei_rong, "完成": yi_wan_cheng})
            hang = f.readline()
        f.close()
    except Exception as e:
        print(f"加载数据时出错：{e}")


def bao_cun_shu_ju():
    """把待办数据保存到文件"""
    try:
        f = open(wen_jian_ming, "w", encoding="utf-8")
        for item in todo_list:
            flag = "1" if item["完成"] else "0"
            f.write(f"{flag}|{item['内容']}\n")
        f.close()
    except Exception as e:
        print(f"保存数据时出错：{e}")


def xian_shi_lie_biao():
    """显示所有待办事项"""
    if len(todo_list) == 0:
        print("  （还没有待办事项）")
        return
    
    print(f"  共 {len(todo_list)} 项：")
    print()
    for i, item in enumerate(todo_list):
        xu_hao = i + 1
        if item["完成"]:
            zhuang_tai = "✅ 已完成"
        else:
            zhuang_tai = "⬜ 未完成"
        print(f"  {xu_hao:>2}. [{zhuang_tai}] {item['内容']}")


def tian_jia():
    """添加待办"""
    nei_rong = input("请输入待办内容：").strip()
    if nei_rong == "":
        print("内容不能为空哦")
        return
    todo_list.append({"内容": nei_rong, "完成": False})
    bao_cun_shu_ju()
    print("添加成功！")


def wan_cheng():
    """标记完成"""
    xian_shi_lie_biao()
    if len(todo_list) == 0:
        return
    hao_ma = input("请输入要标记完成的序号：")
    if not hao_ma.isdigit():
        print("请输入数字序号")
        return
    idx = int(hao_ma) - 1
    if idx < 0 or idx >= len(todo_list):
        print("序号不对哦")
        return
    todo_list[idx]["完成"] = True
    bao_cun_shu_ju()
    print("已标记为完成！")


def shan_chu():
    """删除待办"""
    xian_shi_lie_biao()
    if len(todo_list) == 0:
        return
    hao_ma = input("请输入要删除的序号：")
    if not hao_ma.isdigit():
        print("请输入数字序号")
        return
    idx = int(hao_ma) - 1
    if idx < 0 or idx >= len(todo_list):
        print("序号不对")
        return
    shan_diao = todo_list.pop(idx)
    bao_cun_shu_ju()
    print(f"已删除：{shan_diao['内容']}")


# 程序启动，先加载数据
jia_zai_shu_ju()

# 主循环
while True:
    print()
    print("-" * 35)
    print("  1 - 查看待办")
    print("  2 - 添加待办")
    print("  3 - 标记完成")
    print("  4 - 删除待办")
    print("  5 - 退出程序")
    print("-" * 35)
    
    xuanze = input("请选择操作(1-5)：")
    
    if xuanze == "5":
        print("再见！记得完成待办哦～")
        break
    elif xuanze == "1":
        print()
        xian_shi_lie_biao()
    elif xuanze == "2":
        print()
        tian_jia()
    elif xuanze == "3":
        print()
        wan_cheng()
    elif xuanze == "4":
        print()
        shan_chu()
    else:
        print("选项不对，请重新选择")
