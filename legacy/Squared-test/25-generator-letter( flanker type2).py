import string

letters = string.ascii_uppercase  # 大写字母表 "A" 到 "Z"

for fixed in letters:
    for other in letters:
        if fixed == other:
            continue
        left = fixed * 2 + other + fixed * 2
        right = other * 2 + fixed + other * 2
        # 用制表符连接两列
        print(left + "\t" + right)
