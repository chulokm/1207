a = (float) (input ("请输入第一个数字: "))
b =(float) (input ("请输入第二个数字: "))
symbol = (input ("请输入计算符号: "))
match symbol:
        case  "+" :
            print(f"a + b={a+b:.21f}")
        case  "-" :
            print(f"a - b={a-b:.21f}")
        case  "*" :
            print(f"a * b={a*b:.21f}")
        case  "/"  if b != 0:
            print(f"a / b={a/b:.21f}")
        case  _ :
            print("无效的表达式.\n")
    