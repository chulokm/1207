num = 100
minor = 3
i = 0
allm = 0
for count in range(num , 500 ):
    if count % 3 == 0 :
        allm += count
        i += 1
        print(f"当期和为{allm}\n")
        print(f"第{i}次\n")
else:
    print("计算结束\n")
       
for i in range(1,10):
    for j in range(1,10):
        if (i+j) % 2 == 0:
            print(1,end=" ")
        else :
            print(2,end=" ")
    print()
    