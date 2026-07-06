cart = {}
menu = """
######购物车系统#####
#    1.新增商品     #
#    2.修改商品     #
#    3.删除商品     #
#    4.当前商品     #
#    5.商品结算     #
#    6.退出系统     #
#####################
"""
print(menu)
while True:
    choice = input("\n请输入1-6选择操作页面")
    match (choice):
        case"1":
            goods_name = input("请输入商品名:")
            goods_price = float(input("请输入商品价格:"))
            goods_amount = int(input("请输入商数量:"))
            if goods_name in cart:
                print("该商品已存在")
                continue
            else:
                cart[goods_name] = {'商品价格':goods_price,'商品数量':goods_amount}
                print("添加成功!")
                continue
        case"2":
            choice2 = input("请输入想要更改的商品:")
            if choice2 in cart:
                choice21 = input("请输入要更改的项(价格&数量&全部修改):")
                match(choice21):
                    case"价格":
                        goods_price = float(input("请输入新的商品价格"))
                        cart[choice2]['商品价格'] = goods_price
                        print("修改成功!")
                        continue
                    case"数量":
                        goods_amount = int(input("请输入新的商品数量"))
                        cart[choice2]['商品数量'] = goods_amount
                        print("修改成功!")
                        continue
                    case"全部修改":
                        goods_price = float(input("请输入新的商品价格"))
                        goods_amount = int(input("请输入新的商品数量"))
                        cart[choice2] = {'商品价格':goods_price,'商品数量':goods_amount}
                        print("修改成功!")
                        continue
                    case"退出":
                        pass
                    case _:
                        print("输入有误!")
                        continue
            else:
                print("该商品不在购物车中!")
                continue
        case"3":
            dele = input("请输入要删除的商品:")
            if dele in cart:
               del cart[dele]
               print("删除成功!")
               continue
            else:
                print("该商品不在购物车中!")
                continue
        case"4":
            print("====当前商品====")
            for index,goods in enumerate(cart,1):
                print(f"{index},商品名称:{goods},单价:{cart[goods]['商品价格']},数量:{cart[goods]['商品数量']}")
                continue
        case"5":
            print("\n=======计算中=======\n")
            total = 0 
            for index,goods in enumerate(cart,1):
                current_total = (cart[goods]['商品价格'])*(cart[goods]['商品数量'])
                total += current_total
            print(f"当前商品总价为{total}")
            continue
        case"6":
            print("再见~")
            break
        case _;
            print("无法识别的操作!")
            continue