n = int(input("请输入学生人数："))
subjects = []
subject_count = int(input("请输入科目数量："))
for i in range(subject_count):
    sub = input(f"请输入第{i+1}个科目名称：")
    subjects.append(sub)
students = []
for i in range(n):
    name = input(f"\n请输入第{i+1}个学生的姓名：")
    scores = {}
    total = 0
    for sub in subjects:
        score = float(input(f"请输入{name}的{sub}成绩："))
        scores[sub] = score
        total += score
    avg = total / subject_count
    students.append({
        "name": name,
        "scores": scores,
        "total": total,
        "avg": avg
    })
print("\n===== 每个学生的总分和平均分 =====")
for stu in students:
    print(f"{stu['name']} - 总分：{stu['total']:.2f}，平均分：{stu['avg']:.2f}")
print("\n===== 各科成绩统计 =====")
for sub in subjects:
    scores_list = [stu["scores"][sub] for stu in students]
    min_score = min(scores_list)
    max_score = max(scores_list)
    avg_score = sum(scores_list) / len(scores_list)
    print(f"{sub} - 最低分：{min_score:.2f}，最高分：{max_score:.2f}，平均分：{avg_score:.2f}")
print("\n===== 成绩优秀（平均分>90）的学生 =====")
excellent_students = [stu for stu in students if stu["avg"] > 90]
if excellent_students:
    for stu in excellent_students:
        print(f"{stu['name']} - 平均分：{stu['avg']:.2f}")
else:
    print("没有平均分大于90的学生")
