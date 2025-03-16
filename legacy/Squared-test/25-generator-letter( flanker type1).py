import string


letters = string.ascii_uppercase

for first in numnber:
    for second in letters:
        if first == second:
            continue
        # 使用制表符 '\t' 作为分隔符
        print(first * 5 + "\t" + second * 5)
