import random
num = random.randint(1,100)
answer = num
while True:
    user = int(input("请输入你猜的一个数字: "))
    if user == num:
        print("恭喜你猜对了!")
        exit()
    elif user == 000:
        print("答案是: ",answer)
    elif user >= num:
        if abs(user -num) <= 10:
            print("大了一点哦~")
        else :
            print("大得有点多哦~")
    elif user <= num:
        if abs(user -num) <= 10:
            print("小了一点哦~")
        else :
            print("小得有点多哦~")
    elif user > 100:
        print("这超出范围啦!")
    else:
        print("这不是数字吧!")