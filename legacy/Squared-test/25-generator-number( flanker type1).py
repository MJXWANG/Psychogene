for first in range(1, 10):
    for second in range(1, 10):
        if first == second:
            continue
        # 使用制表符作为分隔符，生成类似 "11111	22222" 的输出
        print(str(first) * 5 + "\t" + str(second) * 5)
