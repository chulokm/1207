menu = """
######购物系统#######
#    1.新增商品     #
#    2.修改商品     #
#    3.删除商品     #
#    4.当前商品     #
#    5.商品结算     #
#    6.退出系统     #
#####################
"""
print(menu)
def purchase (commodity):
    while True:
        stuff = input("请输入商品名称:")
        praise = float(input("请输入商品价格:"))
        amount = int(input("请输入商品数量:"))
        commodity[stuff] = {"商品价格":praise,"商品数量":amount}
        print("添加成功!")
        choice = input("输入1继续添加商品,按其他任意键退出:")
        if choice != "1":
            break
    return commodity
def modify (commodity): 
    choice2 = input("请输入想要更改的商品:")
    if choice2 in commodity:
            choice21 = input("请输入要更改的项(价格&数量&全部修改):")
            match choice21:
                case"价格":
                    goods_price = float(input("请输入新的商品价格"))
                    commodity[choice2]['商品价格'] = goods_price
                    print("修改成功!")
                case"数量":
                    goods_amount = int(input("请输入新的商品数量"))
                    commodity[choice2]['商品数量'] = goods_amount
                    print("修改成功!")
                case"全部修改":
                    goods_price = float(input("请输入新的商品价格"))
                    goods_amount = int(input("请输入新的商品数量"))
                    commodity[choice2] = {'商品价格':goods_price,'商品数量':goods_amount}
                    print("修改成功!")
                case"退出":
                    return
                case _:
                    print("输入有误!")
    else:
            print("该商品不在购物车中!")
    return commodity
def delete (commodity):
    dele = input("请输入要删除的商品:")
    if dele in commodity:
        del commodity[dele]
        print("删除成功!")
    else:
        print("该商品不在购物车中!")
    return commodity
def current (commodity):
    print("====当前商品====")
    for index,goods in enumerate(commodity,1):
        print(f"{index},商品名称:{goods},单价:{commodity[goods]['商品价格']},数量:{commodity[goods]['商品数量']}")
def checkout (commodity):
    total = 0
    m = 0
    for i in commodity.values():
        p = i["商品价格"]
        n = i["商品数量"]
        total += p * n
        m += n
    freight = m * 3
    total = round(total,2)
    return total,freight
def coupon (total):
    if total < 5000:
            print("商品金额需要满5000元才能使用优惠券和积分!")
            return total
    else:
            totaling = 0
            ch = int(input("选择使用优惠券输入1,使用积分输入2(只能同时使用一个),不使用按任意键"))
            if ch == 1:
                    coupons = input("请输入优惠券类型(抵扣券/折扣券)")
                    if coupons == "抵扣券":
                        couponm = int(input("请输入抵扣券金额:"))
                        totaling = total - couponm
                        print(f"券后总价为{totaling}")
                        if totaling <= 0:
                            print("使用优惠券不能超过商品总价!")
                    elif coupons == "折扣券":
                        couponz = float(input("请输入折扣券折数:"))
                        if couponz > 0 and couponz < 10:
                            totaling = total * (couponz * 0.1)
                            print(f"券后总价为{totaling}")
                        elif couponz > 10 and couponz < 100:
                            totaling = total * (couponz * 0.01)
                            print(f"券后总价为{totaling}")
                        else:
                            print("无效的折数!")
                        if totaling <= 0:
                            print("使用优惠券不能超过商品总价!")
                    total = round(totaling,2)
            elif ch == 2:
                    pointsist = int(input("请输入当前积分:"))
                    pointsable = pointsist // 100 
                    while True:
                        print(f"当前积分可抵扣{pointsable}元")
                        use = int(input("请输入抵扣金额:"))
                        if use > pointsable:
                            print("超出当前可使用积分!")
                        elif use <= pointsable:
                            totaling = total - use
                            print(f"券后总价为{totaling}")
                            break
                    if totaling <= 0:
                        print("使用积分的抵扣不能超过商品总价!")
                    total = round(totaling,2)
            else:
                print("直接付款----")
    return total
def main():
    cart = {}
    money = 0
    n = 0
    p = 0
    while True:
        choice = input("请输入操作选项:")
        match choice:
            case"1":
               cart = purchase(cart)
            case"2":
                cart = modify(cart)
            case"3":
                cart = delete(cart)
            case"4":
                current(cart)
            case"5":
              money= checkout(cart)
              n = money[0]
              p = money[1]
              print(f"商品总价为{n},运费为{p}")
              moneying = coupon(n)
              n = moneying
              pay = n + p
              print(f"结算完成,应付{pay}")
              break
            case _:
                print("无效的操作!")
print("欢迎光临~")
main()