import sys
class AAS:
    def __init__(self):
        self.students = {}
    def add(self,need_raise = False):#判断
        self.name = input("请输入学生名字:")
        if self.name in self.students:
            print("该学生已存在!")
            return
        try:
            self.china = float(input(f"请输入{self.name}的语文成绩:"))
            self.math = float(input(f"请输入{self.name}的数学成绩:"))
            self.english = float(input(f"请输入{self.name}的英语成绩:"))
            self.total = self.china + self.math + self.english
            self.students[self.name] = {"语文成绩":self.china,
                                                        "数学成绩":self.math,
                                                        "英语成绩":self.english,
                                                        "总分": self.total}
            print(f"已添加学生{self.name}!")
            return self.students
        except ValueError as e:
            print(f"输入信息有误,请输入数字,错误信息:{e}")
            if need_raise:
                raise
            else:
                return
    def current(self):
        edit = input("请输入想要查询的学生信息:")
        if edit in self.students:
            print(f"{edit}语文成绩:{self.students[edit]['语文成绩']},数学成绩:{self.students[edit]['数学成绩']},英语成绩:{self.students[edit]['英语成绩']},总分:{self.students[edit]["总分"]}")
    def currentall(self):
        if not self.students:
                print("当前系统内未录入学生成绩!")
                return
        print("======当前学生信息======")
        for index,studentv in enumerate(self.students,1):
            print(f"第{index}位学生:{studentv}语文成绩:{self.students[studentv]['语文成绩']},数学成绩:{self.students[studentv]['数学成绩']},英语成绩:{self.students[studentv]['英语成绩']}总分:{self.students[studentv]["总分"]}")
        print("=====班级成绩概况=====")
        score_china = []  
        name_china = []   
        score_math = []
        name_math = []
        score_eng = []
        name_eng = []
        for name, info in self.students.items():
            score_china.append(info["语文成绩"])
            name_china.append(name)
            score_math.append(info["数学成绩"])
            name_math.append(name)
            score_eng.append(info["英语成绩"])
            name_eng.append(name)
        s_c = score_china.copy()
        n_c = name_china.copy()
        for i in range(len(s_c)-1):
            for j in range(len(s_c)-1-i):#冒泡排序,最大的分好在最后,就不再碰
                if s_c[j] > s_c[j+1]:
                    s_c[j], s_c[j+1] = s_c[j+1], s_c[j]
                    n_c[j], n_c[j+1] = n_c[j+1], n_c[j]
        avg_c = sum(s_c)/len(s_c)
        print(f"语文最高:{s_c[-1]}({n_c[-1]}),最低:{s_c[0]}({n_c[0]}),平均:{avg_c:.2f}")
        s_m = score_math.copy()
        n_m = name_math.copy()
        for i in range(len(s_m)-1):
            for j in range(len(s_m)-1-i):
                if s_m[j] > s_m[j+1]:
                    s_m[j], s_m[j+1] = s_m[j+1], s_m[j]
                    n_m[j], n_m[j+1] = n_m[j+1], n_m[j]
        avg_m = sum(s_m)/len(s_m)
        print(f"数学最高:{s_m[-1]}({n_m[-1]}),最低:{s_m[0]}({n_m[0]}),平均:{avg_m:.2f}")
        s_e = score_eng.copy()
        n_e = name_eng.copy()
        for i in range(len(s_e)-1):
            for j in range(len(s_e)-1-i):
                if s_e[j] > s_e[j+1]:
                    s_e[j], s_e[j+1] = s_e[j+1], s_e[j]
                    n_e[j], n_e[j+1] = n_e[j+1], n_e[j]
        avg_e = sum(s_e)/len(s_e)
        print(f"英语最高:{s_e[-1]}({n_e[-1]}),最低:{s_e[0]}({n_e[0]}),平均:{avg_e:.2f}")
    def alter(self):
        stu = self.students
        edit = input("请输入需要修改信息的学生:")
        if edit in self.students:
            subject = input("请输入需要修改的科目(语文/数学/英语):")
            try:
                match subject:
                        case"语文":
                            new_china = float(input("请输入新的语文成绩:"))                    
                            self.students[edit]["语文成绩"] = new_china
                        case"数学":                   
                            new_math = float(input("请输入新的数学成绩:"))                 
                            self.students[edit]["数学成绩"] = new_math
                        case"英语":                            
                            new_english = float(input("请输入新的英语成绩:"))                         
                            self.students[edit]["英语成绩"] = new_english                          
                        case _:
                            print("无效的输入!")
                            return
            except ValueError as e:
                print(f"输入信息有误,请输入数字,错误信息:{e}")
        else:
            print(f"名为{edit}的学生不存在!")
            return
        stu_score = self.students[edit]
        stu_score["总分"] =  stu_score["语文成绩"] +  stu_score["数学成绩"] +  stu_score["英语成绩"]
        print(f"学生{edit}的{subject}成绩已修改")
        return self.students
    def delete(self):
        edit = input("请输入需要删除的学生:")
        if edit in self.students:
            del self.students[edit]
            print("学生信息已删除!")
        else:
            print(f"名为{edit}的学生不存在!")
            return
        return self.students
    def leave(self):
        choice= input("是否要退出系统?(是/否)")
        if choice == "是":
            print("已退出")
            sys.exit()
        elif choice == "否":
            print("继续当前操作---")
        else:
            print("无效的操作!")
    def main (self):
        menu = """
        #####班级成绩管理系统###########
        #      1.添加学生及成绩信息    #
        #      2.修改学生及成绩信息    # 
        #      3.删除学生及成绩信息    # 
        #      4.查询学生及成绩信息    # 
        #      5.班级学生一览          #
        #      6.退出系统              #
        ################################
        """
        print(menu)
        classm = AAS()
        while True:
            try:
                print("======添加第一份学生信息以开始======")
                classm.add(need_raise=True)#判断:仅开始输入时需要raise抛出异常继续循环
                break
            except ValueError :
                print("输入格式有误无法开始系统,请重新输入!")
        while True:
            try:
                ch = int(input("\n请选择当前操作(1~6):"))
            except ValueError as e:
                print(f"输入有误,请输入1~6进行操作,错误信息:{e}")
                continue
            match ch:
                case 1:
                    classm.add()
                case 2:
                    classm.alter()
                case 3:
                    classm.delete()
                case 4:
                    classm.current()
                case 5:
                    classm.currentall()
                case 6:
                    classm.leave()
                case _:
                    print("输入无效或超出范围,请输入1~6选择操作!")
again = AAS()
again.main()