num = 0.0
minor = 2.0
allm = 0.0
i = 0
while num >= 0:
    num +=  1
    if num % minor == 0:
        allm += num
        print(f"当前总和为:{allm}\n")
        i += 1
        print(f"第{i}次\n")
else:
        print("计算完成\n")