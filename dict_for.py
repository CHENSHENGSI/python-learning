# 1.字典是什么？
# 字典：一种无序，可变的键值对集合
# 格式：{键：值}
# 键必须是不可变的数据类型（字符串，数字，元组），值可以是任意类型。



# 2.字典的基本操作——————对 键 进行操作
# 创建字典
student = {'name':'张三','age':20,'major':'计算机科学'}
score = {'数学':90,'英语':78,'编程':93}

# 访问元素--通过键
print(student['name'])   # 返回’张三‘
print(score['编程'])        # 返回 93

# 修改元素--通过键
student['age'] = 45      # student = {'name':'张三','age':45,'major':'计算机科学'}
score['英语'] = 100      # score = {'数学':90,'英语':100,'编程':93}
print(student,score)

# 添加新键值对
student['hobby'] = '唱歌'       # student = {'name':'张三','age':45,'major':'计算机科学','hobby':'唱歌'}
score['语文'] = 89              # score = {'数学':90,'英语':100,'编程':93,'语文'：89}
print(student,score)

# 删除元素
del student['hobby']            # student = {'name':'张三','age':45,'major':'计算机科学'}
removed = score.pop('数学')     # score = {'英语':100,'编程':93,'语文'：89}
print(student,score)

# 获取长度
print(len(student))     # 3




# 3.字典常用方法
person = {'name':'lenu','age':23,'slogen':'要做就要做好','city':'重庆'}

#获取所有键--变量.keys()
keys = person.keys()     # dict_keys(['name', 'age', 'slogen', 'city'])
keys_list = list(keys)   # 转换为列表
print(keys,keys_list)

# 获取所有值--变量.values()
values = person.values()  # dict_values(['lenu', 23, '要做就要做好', '重庆'])
print(values)

# 获取所有键值对--变量.items()
items = person.items()    # dict_items([('name', 'lenu'), ('age', 23), ('slogen', '要做就要做好'), ('city', '重庆')])
print(items)

# 安全访问（键不存在时返回默认值）
age = person.get('age',0)   # 23
salary = person.get('salary',0)   # 0 因为没有salary这个键
print(age,salary)

# 检查键是否存在
if 'city' in person:
    print('城市信息存在！')

# 清空字典
person.clear()



# 4. for循环基础
# 遍历列表
fruits = ['apple','banana','cherry','watermalen']
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in 'python':
    print(char)

# 遍历字典：
student = {'name':'张三','age':20,'major':'计算机科学'}
# print(student['name'])
for key in student:
    print(key,student[key])  # 遍历键，后面的这个student[key]返回的是对应的值


for key,value in student.items():
    print(f'{key}:{value}')  # 遍历键值对

# 使用range()生成数字序列
for i in range(5):
    print(i)

for i in range(2,8):
    print(i)

for i in range(1,10,2):
    print(i)




# 5.循环控制语句
# break：提前结束循环
for i in range(10):
    if i == 5:
        break     # 当i=5的时候结束循环
    print(i)


# continue: 跳过当前迭代
for i in range(10):
    if i == 5:      #跳过i=5的这次循环
        continue   
    print(i)



# else:循环正常结束（非break中断）后执行
for i in range(10):
    print(i)
else:
    print('循环正常结束！')