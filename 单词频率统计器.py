import string #导入字符串处理模块
text = '''
Python is an interpreted high-level programming language for general-purpose programming.
Python has a design philosophy that emphasizes code readability.
Python is a great language for beginners.
'''


# 1.清理文本 
cleaned_text = text.lower()

# 去除标点符号
print('标点符号：',string.punctuation)   #string.punctuation输出结果： !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
for punctuation in string.punctuation:
    cleaned_text = cleaned_text.replace(punctuation,'')  # 遍历每个标点符号，用空字符串替换掉

# 2.分割单词
words = cleaned_text.split()    #将字符串按空白字符（空格、换行等）分割成单词列表

# 3.统计频率(核心！)
word_count = {}
for word in words:
    if word in word_count:   #遍历每个单词，若是单词已经在字典中，则计数加一，否则将单词加入字典并设置计数为1
        word_count[word] += 1
    else:
        word_count[word] = 1

# 解析：过程：
# 1.word = 'python'--->不在字典--->word_count={'python':1}
# 2.word = 'is' --->不在字典---> word_count={'python'：1,'is'：1}
# 3.word = 'python' --->在字典---> word_count={'python'：2,'is'：1}
# 4.word = 'great' --->不在字典---> word_count={'python'：2,'is'：1,'great':1}


# # 4.排序
sorted_words = sorted(word_count.items(),key=lambda x:x[1],reverse=True)  #key=lambda x:x[1]表示按照每个键值对的第二个元素（即计数）进行排序
# 解析：
# word_count.items() 返回键值对列表  例如：[('python',3),('is',2)]
# sorted()排序，key指定排序依据
# lambda x:x[1] 表示按每个元组的第二个元素（即次数）排序
# reverse=True 表示降序（从大到小）
# 等价写法（更易理解）：
#def get_count(item):
    # return item[1] #返回次数

# sorted_words = sorted(word_count.items(),key=get_count,reverse=True)




# 输出结果
print('==============单词频率统计=================')
for word,count in sorted_words[:10]:   #只显示前10个
    print(f'{word}:{count}次')





# # 自我练习
# # 1.清理文本
# cleaned_text= text.lower()
# # 去除标点
# for punctuation in string.punctuation:
#     cleaned_text = cleaned_text.replace(punctuation,'')

# words = cleaned_text.split()

# # 2.统计单词频率
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
    
# # 3.排序
# sorted_words = sorted(word_count.items(),key=lambda x: x[1],reverse=True)

# # 4.输出
# print('=================单词频率统计================')
# for word,count in sorted_words[:10]:
#     print(f'{word}:{count}次！')


