# -*- coding: utf-8 -*-
# 凯撒密码加密解密工具
# 凯撒密码就是把字母往后移动固定位数
# 比如偏移3位，A变成D，B变成E...
# 新手练习：字符操作、ASCII码、函数

print("=" * 45)
print("       🔐 凯撒密码小工具")
print("=" * 45)
print()
print("凯撒密码：把每个字母往后移动固定位数")
print("比如偏移3位，A→D，b→e，Z→C（循环回来）")
print()


def jia_mi(ming_wen, pian_yi):
    """加密函数：明文 -> 密文"""
    mi_wen = ""
    for zi_fu in ming_wen:
        if zi_fu.isupper():
            # 大写字母：A的ASCII码是65
            # 先算出相对位置，加偏移，取模26，再转回字符
            wei_zhi = ord(zi_fu) - ord('A')
            xin_wei_zhi = (wei_zhi + pian_yi) % 26
            xin_zi_fu = chr(xin_wei_zhi + ord('A'))
            mi_wen = mi_wen + xin_zi_fu
        elif zi_fu.islower():
            # 小写字母：a的ASCII码是97
            wei_zhi = ord(zi_fu) - ord('a')
            xin_wei_zhi = (wei_zhi + pian_yi) % 26
            xin_zi_fu = chr(xin_wei_zhi + ord('a'))
            mi_wen = mi_wen + xin_zi_fu
        else:
            # 不是字母的原样保留（空格、数字、标点都不变）
            mi_wen = mi_wen + zi_fu
    return mi_wen


def jie_mi(mi_wen, pian_yi):
    """解密函数：密文 -> 明文
    解密就是反向偏移，相当于加密时偏移量取负数
    """
    return jia_mi(mi_wen, -pian_yi)


def po_jie(mi_wen):
    """穷举破解：因为只有26种可能，全部试一遍"""
    print()
    print("穷举所有可能的偏移量：")
    print("-" * 40)
    for i in range(26):
        jie_guo = jie_mi(mi_wen, i)
        print(f"  偏移{i:>2}: {jie_guo}")
    print("-" * 40)
    print("看看哪一行最像正常的英文～")


# 主循环
while True:
    print("请选择操作：")
    print("  1 - 加密")
    print("  2 - 解密")
    print("  3 - 穷举破解（26种可能）")
    print("  4 - 退出")
    print()
    
    xuanze = input("请输入选项(1-4)：")
    
    if xuanze == "4":
        print("再见！注意安全～")
        break
    
    if xuanze not in ["1", "2", "3"]:
        print("选项不对呢")
        print()
        continue
    
    wen_ben = input("请输入文本：")
    
    if xuanze == "3":
        po_jie(wen_ben)
        print()
        continue
    
    # 加密或解密需要偏移量
    pian_yi_str = input("请输入偏移量(1-25)：")
    if not pian_yi_str.isdigit():
        print("偏移量必须是数字哦")
        print()
        continue
    
    pian_yi = int(pian_yi_str)
    if pian_yi < 1 or pian_yi > 25:
        print("偏移量在1到25之间")
        print()
        continue
    
    print()
    if xuanze == "1":
        result = jia_mi(wen_ben, pian_yi)
        print(f"明文：{wen_ben}")
        print(f"密文：{result}")
    else:
        result = jie_mi(wen_ben, pian_yi)
        print(f"密文：{wen_ben}")
        print(f"明文：{result}")
    
    print()
