right_act="1207"
right_pwd="15260811"
count=0
time=3
cash="10000"
while True:
        act=input("请输入账号; \n")
        pwd=input("请输入密码; \n")
        if  act==right_act and pwd==right_pwd:
            print(f"欢迎,{right_act}")
            break
        else :
            print("账号或密码错误,请重新输入!")
            count+=1
            if count>=time:
             print("错误次数过多,已自动退出")
             exit()
wcash=input("请输入取出金额; \n")
beleft=input(f"已取出,请拿好,当前账户剩余金额为;{int(cash)-int(wcash)}")
print("再见!")

a=float(input("请输入数字a:"))
b=float(input("请输入数字b:"))
num=(a**5/b**3) -666*(45+33)
print("(a**5/b**3) -666*(45+33)=%.15f"%num)
print("1999/4**9=%.15f"% (1999/4**9))
         
ag = input("请输入年份:  \n")
ago=int(ag)
if ago%400==0 or ago%4==0:
    print("该年份为闰年")
else:
    print("该年份为平年")
     
print("三角形判断\n")
degree1 =   int (input("第一个角度: "))
degree2 =  int (input("第二个角度: "))
degree3 =  int (input("第三个角度: "))

if degree1 + degree2 + degree3 != 180 or  degree1 <=0 or degree2 <= 0 or degree3 <=0 :
    print("该图形不是三角形")
else:
    if degree1 == 90 and degree2 ==45 and degree3 == 45 or degree2 ==90 and degree1 == 45 and degree3 ==45 or degree3 == 90 and degree2 == 45 and degree1== 45:
        print("该三角形为等腰直角三角形")
    elif degree1 == 90 or degree2 ==90 or degree3 == 90:
        print("该三角形为直角三角形")
    elif degree1 == degree2 or degree1 == degree3 or degree2 == degree3:
        print("该三角形为等腰三角形")
    else:
        print("该三角形为普通三角形")

act1 = 123456
pwd1 = 123456
act2 = 2468
pwd2 = 2468
time = 3
count = 0
while True:
    act = input("请输入账号: ")
    pwd = input ("请输入密码: ")
    if (act == "") or (pwd == ""):
        print("账号或密码不能为空!")
        if count >= time:
            print("错误次数过多,已自动退出!")
            exit()
    if (act == act1 and pwd == pwd1) or (act == act2 and pwd == pwd2) :
        print("登陆成功~")
        break
    else :
        print("账号或密码错误,请重新输入!")
        count +=1
        if count >= time:
            print("错误次数过多,已自动退出!")
            exit()
   