import ollama

students = {}
menu = """
#####班级成绩管理系统###########
#      1.添加学生及成绩信息    #
#      2.修改学生及成绩信息    # 
#      3.删除学生及成绩信息    # 
#      4.查询学生及成绩信息    # 
#      5.班级学生一览          #
#      6.班级成绩详情统计      #
#      7.AI分析单个学生学情    #
#      8.AI生成班级成绩总结    #
#      9.自然语言AI交互操作    #
#      0.退出系统              #
################################
"""
def ai_chat(prompt):
    res = ollama.chat(
        model="qwen3.5:9b",
        messages=[{"role": "user", "content": prompt}],
        options={"num_ctx": 4096, "temperature": 0.6}
    )
    return res["message"]["content"]

def add_student():
    stu_name = input("请输入学生姓名:")
    try:
        obj_china = float(input(f"请输入{stu_name}的语文成绩:"))
        obj_math = float(input(f"请输入{stu_name}的数学成绩:"))
        obj_english = float(input(f"请输入{stu_name}的英语成绩:"))
        if not (0 <= obj_china <= 100 and 0 <= obj_math <= 100 and 0 <= obj_english <= 100):
            print("成绩必须在0-100之间！")
            return
        students[stu_name] = {'语文成绩': obj_china, '数学成绩': obj_math, '英语成绩': obj_english}
        print("录入成功!")
    except ValueError:
        print("输入的成绩不是有效数字！")

def edit_student():
    choice1 = input("请输入需要修改成绩的学生:")
    if choice1 not in students:
        print("未找到该学生!")
        return
    target_stu = choice1
    choice11 = input("请选择需要更改的科目(语文/数学/英语/全部科目):")
    try:
        if choice11 == "语文":
            new_china = float(input("请输入新的语文成绩:"))
            if 0 <= new_china <= 100:
                students[target_stu]["语文成绩"] = new_china
                print("修改完成!")
            else:
                print("成绩范围0-100")
        elif choice11 == "数学":
            new_math = float(input("请输入新的数学成绩:"))
            if 0 <= new_math <= 100:
                students[target_stu]["数学成绩"] = new_math
                print("修改完成!")
            else:
                print("成绩范围0-100")
        elif choice11 == "英语":
            new_english = float(input("请输入新的英语成绩:"))
            if 0 <= new_english <= 100:
                students[target_stu]["英语成绩"] = new_english
                print("修改完成!")
            else:
                print("成绩范围0-100")
        elif choice11 == "全部科目":
            new_china = float(input("请输入新的语文成绩:"))
            new_math = float(input("请输入新的数学成绩:"))
            new_english = float(input("请输入新的英语成绩:"))
            if 0 <= new_china <= 100 and 0 <= new_math <= 100 and 0 <= new_english <= 100:
                students[target_stu]["语文成绩"] = new_china
                students[target_stu]["数学成绩"] = new_math
                students[target_stu]["英语成绩"] = new_english
                print("修改完成!")
            else:
                print("成绩超出0-100范围！")
        else:
            print("输入科目有误!")
    except ValueError:
        print("成绩必须输入数字！")

def del_student():
    choice2 = input("请输入需要删除的学生:")
    if choice2 in students:
        del students[choice2]
        print("已删除!")
    else:
        print("未找到该学生!")

def search_student():
    choice3 = input("请输入需要查询的学生:")
    if choice3 in students:
        info = students[choice3]
        print(f"\n{choice3} 各科成绩：")
        print(f"语文：{info['语文成绩']}  数学：{info['数学成绩']}  英语：{info['英语成绩']}")
    else:
        print("未找到该学生!")

def show_all_student():
    print("=====当前班级学生成绩=====")
    if not students:
        print("暂无学生数据")
        return
    for index, studentv in enumerate(students, 1):
        data = students[studentv]
        print(f"第{index}个学生:{studentv} | 语文:{data['语文成绩']} 数学:{data['数学成绩']} 英语:{data['英语成绩']}")

def class_stat():
    if not students:
        print("当前系统内未录入学生成绩!")
        return
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

def ai_analyze_single():
    stu_name = input("请输入要分析的学生姓名：")
    if stu_name not in students:
        print("无该学生数据")
        return
    data = students[stu_name]
    prompt = f"""你是专业班主任，分析学生{stu_name}的成绩：语文{data['语文成绩']}，数学{data['数学成绩']}，英语{data['英语成绩']}。
输出内容：1.各科强弱分析 2.短板提升建议 3.整体学习评语，语言简洁贴合中小学教学"""
    print("\n=====AI学情分析=====")
    res = ai_chat(prompt)
    print(res)

def ai_class_summary():
    if not students:
        print("暂无班级数据")
        return
    all_data = ""
    for name, score in students.items():
        all_data += f"{name}:语文{score['语文成绩']},数学{score['数学成绩']},英语{score['英语成绩']}\n"
    prompt = f"""你是班主任，根据下面全班学生成绩写一份班级成绩总结，包含：整体平均分判断、偏科学生识别、各科学习问题、后续教学改进方案。
全班成绩：
{all_data}"""
    print("\n=====AI班级成绩总结=====")
    res = ai_chat(prompt)
    print(res)

def ai_nlp_control():
    print("输入你的操作需求（例如：添加张三 语文80数学90英语85 / 修改李四数学95 / 查询王五 / 生成班级总结），输入quit退出对话")
    while True:
        user_text = input("你的指令：")
        if user_text.lower() == "quit":
            break
        prompt = f"""你是成绩管理系统指令解析助手，系统现有功能：添加学生、修改学生成绩、删除学生、查询学生、查看全班、统计班级、AI分析学生、生成班级总结。
用户输入：{user_text}
现有学生名单：{list(students.keys())}
请只输出标准化操作指令，不要多余文字，格式示例：
【添加】张三 语文88 数学92 英语76
【修改】张三 数学 95
【查询】张三
【删除】张三
【全班一览】
【班级统计】
【单生分析】张三
【班级总结】
"""
        cmd = ai_chat(prompt).strip()
        print(f"解析指令：{cmd}")
        if cmd.startswith("【添加】"):
            parts = cmd.replace("【添加】","").strip().split()
            if len(parts) == 4:
                s_name, c, m, e = parts
                try:
                    score_c = float(c)
                    score_m = float(m)
                    score_e = float(e)
                    if 0 <= score_c <= 100 and 0 <= score_m <= 100 and 0 <= score_e <= 100:
                        students[s_name] = {"语文成绩":score_c,"数学成绩":score_m,"英语成绩":score_e}
                        print(f"已自动录入{s_name}成绩")
                    else:
                        print("成绩超出0-100范围，录入失败")
                except:
                    print("成绩数字解析失败")
        elif cmd.startswith("【修改】"):
            parts = cmd.replace("【修改】","").strip().split()
            if len(parts) ==3:
                s_name, sub, val = parts
                sub_map = {"语文":"语文成绩","数学":"数学成绩","英语":"英语成绩"}
                if s_name in students and sub in sub_map:
                    try:
                        new_val = float(val)
                        if 0 <= new_val <= 100:
                            students[s_name][sub_map[sub]] = new_val
                            print(f"已修改{s_name}{sub}成绩")
                        else:
                            print("成绩超出0-100")
                    except:
                        print("成绩数字错误")
        elif cmd.startswith("【查询】"):
            s_name = cmd.replace("【查询】","").strip()
            if s_name in students:
                print(students[s_name])
            else:
                print("无该学生")
        elif cmd == "【全班一览】":
            show_all_student()
        elif cmd == "【班级统计】":
            class_stat()
        elif cmd.startswith("【单生分析】"):
            s_name = cmd.replace("【单生分析】","").strip()
            if s_name in students:
                prompt = f"""分析学生{s_name}成绩{students[s_name]}，给出学习建议"""
                print(ai_chat(prompt))
            else:
                print("找不到该学生")
        elif cmd == "【班级总结】":
            ai_class_summary()
        else:
            print("无法识别该指令，请重新描述需求")

def main():
    """系统主入口，运行班级成绩管理系统"""
    while True:
        print(menu)
        choice = input("\n请输入功能编号(0退出)：")
        match choice:
            case "1":
                add_student()
            case "2":
                edit_student()
            case "3":
                del_student()
            case "4":
                search_student()
            case "5":
                show_all_student()
            case "6":
                class_stat()
            case "7":
                ai_analyze_single()
            case "8":
                ai_class_summary()
            case "9":
                ai_nlp_control()
            case "0":
                print("系统退出，再见！")
                break
            case _:
                print("无效编号，请输入0-9之间数字")

if __name__ == "__main__":
    main()