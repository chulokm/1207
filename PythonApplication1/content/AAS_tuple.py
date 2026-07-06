menu = """
#####班级成绩管理系统###########
#      1.添加学生及成绩信息    #
#      2.修改学生及成绩信息    # 
#      3.删除学生及成绩信息    # 
#      4.查询学生及成绩信息    # 
#      5.班级学生一览          #
#      6.班级成绩详情          #
#      7.退出系统              #
################################
"""
print(menu)
students = {}
while True:
    choice = input("请输入1-7进行操作")
    match(choice):
        case"1":
            stu_name = input("请输入学生姓名:")
            obj_china =  float(input(f"请输入{stu_name}的语文成绩:"))
            obj_math =  float(input(f"请输入{stu_name}的数学成绩:"))
            obj_english =  float(input(f"请输入{stu_name}的英语成绩:"))
            students[stu_name] = {'语文成绩':obj_china,'数学成绩':obj_math,'英语成绩':obj_english}
            print("录入成功!")
            continue
        case"2":
            choice1 = input("请输入需要修改成绩的学生:")
            if choice1 in students:
                choice11 = input("请选择需要更改的科目(语文/数学/英语/全部科目):")
                match(choice11):
                    case"语文":
                        new_china = float(input("请输入新的语文成绩:"))
                        students[stu_name] = {'语文成绩':new_china}
                        print("修改完成!")
                        continue
                    case"数学":
                        new_math = float(input("请输入新的数学成绩:"))
                        students[stu_name] = {'数学成绩':new_math}
                        print("修改完成!")
                        continue
                    case"英语":
                        new_english = float(input("请输入新的英语成绩:"))
                        students[stu_name] = {'英语成绩':new_english}
                        print("修改完成!")
                        continue
                    case"全部科目":
                        new_china = input("请输入新的语文成绩:")
                        students[stu_name] = {'语文成绩':new_china}
                        new_math = input("请输入新的数学成绩:")
                        students[stu_name] = {'数学成绩':new_math}
                        new_english = input("请输入新的英语成绩:")
                        students[stu_name] = {'英语成绩':new_english}
                        print("修改完成!")
                        continue
                    case _:
                        print("输入有误!")
            else:
                print("未找到该学生!")
                continue
        case"3":
            choice2 = input("请输入需要删除的学生:")
            if choice2 in students:
                del students[choice2]
                print("已删除!")
                continue
            else:
                print("未找到该学生!")
                continue
        case"4":
            choice3 = input("请输入需要查询的学生:")
            if choice3 in students:
                print(f"{choice3}, 各科成绩:{students[choice3]}")
                continue
            else:
                print("未找到该学生!")
                continue
        case"5":
            print("=====当前班级学生成绩=====")
            for index, studentv in enumerate(students,1):
                print(f"第{index}个学生:{studentv}语文成绩:{students[studentv]['语文成绩']},数学成绩:{students[studentv]['数学成绩']},英语成绩:{students[studentv]['英语成绩']}")
            continue
        case"6":
            if not students:
                print("当前系统内未录入学生成绩!")
                continue
            print("=====班级成绩概况=====")
            score_china = []  
            name_china = []   
            score_math = []
            name_math = []
            score_eng = []
            name_eng = []
            for name, info in students.items():
                score_china.append(info["语文成绩"])
                name_china.append(name)
                score_math.append(info["数学成绩"])
                name_math.append(name)
                score_eng.append(info["英语成绩"])
                name_eng.append(name)
            s_c = score_china.copy()
            n_c = name_china.copy()
            for i in range(len(s_c)-1):
                for j in range(len(s_c)-1-i):
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
            continue
        case"7":
            print("再见~")
            break
        case _:
            print("无效的输入操作!")
            continue