# 学生信息管理系统（字典版）
# 要求：
#1.创建一个空字典
# 2.添加3个学生信息，每个学生包括：姓名、年龄、专业、成绩（列表）
# 3.实现功能：
#   1.添加新学生
#   2.查找学生信息
#   3.计算每个学生的平均分
#   4.找出所有不及格的学生

students = {}


# 添加初始学生
# 每个键值对是一个元组（,），即格式为（'001'，{'name':'lenu','age':23,'major':'计算机','scores':[85,90,78]})
students['001'] = {
    'name':'lenu',
    'age':23,
    'major':'计算机',
    'scores':[85,90,78]
}

students['002'] = {
    'name':'lina',
    'age':25,
    'major':'英语',
    'scores':[67,87,90]
}
    

students['003'] = {
    'name':'jesical',
    'age':24,
    'major':'物理',
    'scores':[78,95,64]
}

# 计算每个学生的平均分：
print('==============学生平均分=================')

# 另一种写法：#把item分为两步分，即(student_id,info)
for item in students.items():
    student_id = item[0]
    info = item[1]

for  student_id,info in  students.items():
    # print(type(students.items))
    average_score = sum(info['scores'])/len(info['scores'])
    print(f'{info['name']}的平均分为：{average_score:.1f}')
    
# 查找不及格的学生
print('\n===============不及格科目学生================')
for student_id,info in students.items():
    falling_subjects = []
    for i,score in enumerate(info['scores']):  # enumerate:在遍历列表时，用enumerate可以同时获得索引和值
        if score < 60:                              # enumerate(info['score'])会生成类似[(0,85),(1,90),(2,78)]的可迭代对象
            falling_subjects.append(f'第{i+1}门课')  # 
    
    if falling_subjects:
        print(f'{info['name']}有{','.join(falling_subjects)}门课不及格！')  #join语法：'分隔符'.join(字符串列表)  输出格式为："第1门课，第3门课"
    

# 添加学生
def add_students():
    student_id = input('请输入学生id:')
    if student_id in students:
        print('该学生学号已存在，请重新输入：')
        return
    
    name = input('请输入新添加的学生名：')
    age = input('请输入学生年龄：')
    major = input('请输入学生专业：')
    scores = input('请依次输入学生的三门成绩(用空格隔开):')
    
    students[student_id] = {
        'name':name,
        'age':age,
        'major':major,
        'scores':scores
    }
# 添加一个新学生
add_students()
print(students)  #检查是否添加成功
 
