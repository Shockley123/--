dictionary={"love":"爱情"}
keep_going=True
while keep_going:
    types=int(input("请输入（1=学习，2=查询）："))
    if types==2:
        ask=input("请输入单词：")
        if (ask in dictionary):
            print(dictionary[ask])
        else:
            print("错误：字典中没有"+ask)
    else:
        ask=input("请输入单词：")
        asks=input("请输入词语：")
        dictionary[ask]=asks