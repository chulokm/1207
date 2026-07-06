"""
s = [16,17,True,19.01,"aaa"]
print(type(s))
ss = s[0:5:2]
print(ss)
print(s[4])
print(s[-4])
s[2] = "bbb"
print(s[3])
del s[1]
print(s[1])

import copy
a = [1,2,3]
a.append(4)
c = "abc"
b = c
b = copy.deepcopy(a)
print(b)

a = [1,2,3,4,5,6,7]
a.append (8) #末尾加一个元素8
a.insert(0,0) #指定位置加入元素
b=a.pop(0) #指定删除位置元素,并返回被删除元素至一个变量
a.remove(8) #指定删除第一个匹配的元素
c = [9,"abc",3.3]
c.clear() #清空列表
d = [6,9,5,7,2,5,2,5,1,9]
d.sort() #排序
e = d.count(5) #计算元素出现次数
f = len(a) #元素个数
g = sum(a) #元素求和
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)#另外的,min()与max()求最值
y = []
for num in a:
    d.append(num)#a中元素参入d
#for i in d[:]:
#   if d.count(i) > 1:
#        d.remove(i)#遍历数量大于一则删
for i in d:
   if i not in y:
       y.append(i)
       y.sort()
print(y)#等价 y = sorted(set(d))
m = [1,2,3]
n = [1,2,3]
z = [*m,*n]#*解包,等价n+m
l = sorted(set(z))
print(l)
[*t] = 999,555,222#组包
print(t)

even=[]
for num in range(1,21):#等价squares = [num ** 2 for num in range(1,21) if num % 2 ==0]
    squares = num ** 2
    print(squares,end=",")
    if squares % 2 == 0:
        even.append(squares)
print("\n")
print(even)

s = "abcdefghyjk"
b = "ABABABABABA"
c = "123,123,123,123"
d = "     Hello       "
f = "hello,java"
print(s[:-5:-1])#切片
print(b.lower ())#字母转小写
print(s.find("efg"))#寻找该字符(组)第一次出现的 位置(按最后一个输出)
print(s.upper())#字母转大写
print(b.count("A"))#该字符出现次数
print(c.split(","))#依照()内,分割字符串
print(d.strip())#去掉两头的()
print(f.replace("java","pyhon"))#替换字符串内的内容
print(f.startswith("ha"))#判断字符串开头内容
print(f.endswith("va"))#判断字符串结尾内容
print("hello"in f)#判断字符(组)是否存在,返回True或False
print(s)#以上操作都不会改变字符串原本内容

sr = str(input("请输入邮箱地址: "))
small = sr.strip()
if small. find("@") == -1 or small.find(".") == -1:
    print("输入的格式有误,请重新输入!")
else :pwd = int(input("请输入密码:"))
  
sr = str(input("请输入一段回文:"))
if sr == sr[::-1]:
    print("输入正确")
else:print("不是回文")
s = str(input("请输入:"))
sr = s[::-1]
srr = sr.upper()
for srrr in srr:
    print(srrr)

s = (1,2,3)
tup = (999,"abc",3.3,s,999)#不可修改
print(tup[3])
print(type(tup))#类型
print(tup.index(999))#索引
print(tup.count(999))#计数,仅有两个方法
tu = (100,)#单个元素后要带,否则变为int,可以不要括号
print(tu)
a,b,c,d,e = tup#解包,赋值给前面的变量,可以通过()解包嵌套元组
print(s)
a,*b,c,d = tup#*收集相邻无主元素,如在第一位,后面变量从末端领起
print(b)
a = 1
b = 2
c = 3
a,b,c =c,b,a#交换,组包后解包赋值
print(a)

#set 集合:无序,无重复(自动去重),可改.()元组{}集合[]列表""字符串{}字典
se1 = set()#空集合,需要set前缀
print(se1)
se2 = {1,1,2,2,3,3,4,4}#自动去重
print(se2)
se3 = {1,3,5,7,9}
se4 = se2.union(se3)#并集,.union()等价|
print(se4)
se1.add(1)#末尾增加
print(se1)
se1.remove(1)#指定删除
print(se1)
po = se4.pop()#随机删除并返回
print(po)
print(se4)
se6 = se2.difference(se3)#差集(只有前者有后者没有的元素),.difference()与-等价,{s for s in a if s not in b}也等价差集
print(se6)
se7 = se2.intersection(se3)#交集,也可把.intersection()替换成&,等价
print(se7)

dic = {"王林":123,"天天":669,"西西":777}#key不能重复,重复后面的key的value会覆盖前面的value,
#value可以是任意类型,key只能为不可变类型(int,float,bool,str,tuple,frozenset)
print(dic['王林'])
dict1 = {}#空字典,等价dic1 = dict()
dic["王林"] = 600#修改key对应的value
v = dic["王林"]#获取value
dic["五五"] = 700#如果key不存在,则添加一个(key:value)
c = dic.pop("天天")#删除key,并返回被删除的key的value
del dic["西西"]#不会返回,指定删除一个(key:value)
z = dic["五五"]#近似dic.get["天天"],后者当key不存在时会返回None不会报错
#dic.keys()获取所有key,dic.values()获取所有value,dic.items()获取所有key:value键值对
print(dic["王林"],v,c,dic["五五"],z)
for a,b in dic.items():#等价for a in dic.items():   print(f"{a[0]}:{a[1]}")遍历字典
    print(f"{a}:{b}")

def brenam (a,b):#定义新的函数
"""
   
"""#说明
    consequence = round(a / b,2)#round四舍五入,2为保留两位小数
    print(f"相除结果为{consequence}")
    consequence2 = float(a % b)
    print(f"取余结果为{consequence2}")
    return consequence , consequence2#多个值会贮存到tuple中
help(brenam)#展示上面的说明,增加鼠标放在函数上时跳出解释
num = brenam (45,16)#取整tuple
print(num)
a, b = brenam(45,16)#解包取
print(a,b)

def func1 (a):#函数链
    sum = a + 3
    print (f"进入1,{sum}")
    func2(sum)
    print(f"走出1,{sum}")
    return(sum)
def func2(sum):
    sum *= 3
    print (f"进入2,{sum}")
    func3(sum)
    print(f"走出2,{sum}")
def func3(sum):
    sum /= 3
    print (f"进入3,{sum}")
    print(f"走出3,{sum}")
num = func1(3)
print(num)

s = 2
def  area (botton,high):
    ""计算三角形面积
        botton : 三角形的底
        high : 三角形的高
        triangle : 三角形的面积""
    triangle = (botton * high) / 2
    print(f"三角形面积为{triangle}")
    return(triangle)
def count (letter):
    ""判断元音字符个数""
    vowel = "aeiouAEIOU"
    count = 0#函数内定义的变量,为局部变量
    for i in range(0,len(letter)):
        if(letter[i] in vowel):
            count +=1
            print(f"{letter[i]}是元音字母")
        else:print(f"{letter[i]}不是元音字母")
    print(f"共有{count}个元音字母")
    return(count)
def score (students):
    ""判断最分和平均""
    global m 
    global s
    score_max = max(students)
    score_min = min(students)
    score_average = round(sum(students) / len(students),1)
    print(f"最高分为{score_max},最低分为{score_min},平均分{score_average}")
    a = 1000#函数内定义的变量,为局部变量
    m = 1000#函数内定义的变量通过global声明变为全局变量
    s = 3
    return(score_max,score_min,score_average)
help(area)
print(area(6,9))
help(count)
print(count("a""e""y""E""m"))
help(score)
print(score([99,88,55,44,66,89,59,81]))
print(s)
print(m)
m = 100#函数外定义的变量,为全局变量
print(m)
"""
"""
def A (a,b,c=2,*ary,**dic):#可默认,再赋值可覆盖
    #不定长参数:*接受剩余位置参数打包元组,**打包剩余键值对为字典
   s=sum(ary)
   d=max(ary)
   print(a + c + b)
   print(ary,s,d)
   if dic.get("print"):
       print(dic)
A(1,3,7,8,9,55,88, print = "sr")
def B (x,y):
    red = x * y
    return red
def V (x,y,z):
    reds = x/y*z
    return reds
def C (x,y,z,t):
    sums = x + y + z + t
    return sums
def S (x,y):
    last = x/y
    return last
def F (x,y,oper):#接受x和y给一个函数
    return oper(x,y)
def E (x,y,z,oper):#函数有多少个形参就要存几个
    return oper(x,y,z)
result = C(7,B(5,6),F(85,69,S),E(68.5,10.25,99.8,V))#传参可调用函数
print(round(result,1))
nums = {5,33,99,45,12,35,27}#匿名函数lambda,无名字直接一次性调用,自动返回return
list1 = list(map(lambda x: x**2,nums))#map会对每一个数执行函数中的操作
list2 = list(filter(lambda x: x % 2 == 0,nums))#filter会对每一个数进行函数中的判断,True返回
list3 = sorted(nums)#sorted会进行排序(默认升序),元组-列表时需要按(名称,key=函数,升降序)
print(f"{list1}\n{list2}\n{list3}\n")
string= ["sss","match","selees","difficult","nihaoma"]
string.sort(key = lambda x : len(x))
print(string)

def factorial (n):#乘阶
    if not isinstance (n,int):
        raise ValueError ("乘阶仅支持0和大于等于1的整数")#raise抛出ValueError错误并解释
    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)#递归调用(必须有return返回)
print(factorial(1.1))

a: int=3#仅标识,,不强制更改
b: float=0.3
print(a)
def app(score : list[int]) -> float:#指定传入整数列表,最后返回浮点数
   total = sum(score)
   comsequence = total  / 16
   return comsequence
print(app([90,89,95,87,88,97]))
def apps(score: list[int]) -> tuple[int,int,float]:#返回指定元组
    max_score = max(score)
    min_score = min(score)
    average_score = round(sum(score) / len(score),2)
    return max_score,min_score,average_score
print(apps([89,99,76,83,73,91,85]))

import random#引入自带模块
for i in range(10): 
    num = random.randint(1,1000)#random中的一个方法名randint
    print(num)
    if num == 6 or num == 16 or num == 166 or num == 666 or num == 966 or num == 116:
        print("出金");break
from random import randint as intt#等价于上面,指定调入模块中的方法,并另起名称
for i in range(10): 
    num = intt(1,1000)
    print(num)
    if num == 6 or num == 16 or num == 166 or num == 666 or num == 966 or num == 116:
        print("出金");break
import shopping #自定义模块
shopping.main()
print("1 " * 30)#打印30个1
from way1 import*#__all__与*配合,指定导入模块中的部分方法
A()
B()
D()
import shopping#包快速调用,非快速则from包import模块,from包模块import方法(as别名)
shopping.main()
#在init中设置__all__=["模块","模块"],可以from包inport*一键加入
#若不在一个文件夹,可以from绝对路径import模块调用

class Cat:#创建类
#存在pass则不内置属性,
    color = "red"#类属性,全部方法共用,若实例中存在相同属性,则实例中部分覆盖
    def __init__(self,c_name =None ,c_age = None ,c_preference = None):#实例对象
        self.name = c_name
        self.age = c_age
        self.preference= c_preference#方法括号内为形参,传入的数据为实参
    def  express  (self,kind,language):#创建成员方法,仅有self时不用传入实参
         print(f"我是{self.name},是{kind},我会{language}")
    def __del__(self):#对象被删除或程序结束出发
        print("已结束")
    def __str__(self):#直接打印文字,需要return回收
        return f"我是{self.name}"
    def __call__(self):#对象加()自动触发
        print("已启动")#__new__使其最先执行,用以创造实参
c1 = Cat()#创建对象并初始化
c1()
c1.name = "kaze"#当已有内置属性,再动态创建属性,原类内属性需要有默认值
c1.age = 6#若无与原类中属性一致会输出默认值,有则覆盖
c1.preference = "sleep"
c1.food = "bread"
print(c1)#打印地址
print(c1.__dict__)#会打包成字典输出,输出内容需要加.__dict__
c2 = Cat("kiana",21,"mei")#直接传给已有属性数据
c2.express("琪天大圣","哈气")#调用方法并传入实参
print(c2.__dict__)
#对比大小:__lt(小于)le(小于等于)gt(大于)ge(大于等于)eq(相等)ne(不等)
#仅主动判断,类内程序全部统一,不会自主判断大小
#需要return返回,返回boolean值
#__()__为魔法方法,执行时自动调用全部可执行魔法方法

import tools.AAS_def
class1 = tools.AAS_def.AAS()
class1.main()

try:#try-except检测到对应错误会停止中间的代码运行并跳出,,继续执行外面的代码
    a = int("abc")
except ValueError as e:#Exception会铺货绝大部分异常
    print("类型不匹配!",e)
try:
    print(1/0)
except ZeroDivisionError as e:#前加raise会在非异常下主动跳出该类型异常
    print("0不能作为除数!" , e)
try:
    print(c)
except NameError as e:
    print("未定义变量!",e)
try:
    print("abc"+6)
except TypeError as e:
    print("类型运算错误",e)
try:
    listr = [1,2,3,4]
    print(listr[6])
except IndexError as e:#字典无对应key:KeyError
    print("下标溢出!",e)
else:#else会在不触发异常下进行
    print("无异常")
finally:#有finally会在末尾执行,无论程序是否出错
    print("结束-")
class cuo(Exception):#自定义异常,继承括号内作用
    pass
class couw(cuo):#建立子系,细分错误,子系报错父系都能接受,在显示时可做区分和收集
    pass#可单独表达子系,也可通过父系一并表达
    raise 在内层可单独在except后用作抛出异常,外层接收
def f1():
   print("11执行")
   1/0
   1 + "a"
def f2():
    try:
      print("22执行")
      f1()
    except TypeError as e:
     print("异常",e)
def f3():
   print("33执行")
   f2()
try:
    f3()
except ZeroDivisionError as e:
    print("异常",e)
except TypeError as e:
    print("异常",e)
    """
from Qwen import AAS_AI
ch = AAS_AI.main()