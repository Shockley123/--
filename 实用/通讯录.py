import time
#设置
print("==========李劭珂的通讯录==========")
smartphones={'妈妈':18917917063,'爸爸':18918084466,'我':13917798697}#设置通讯录
print(smartphones)
keep_going=True

#创建循环
while keep_going:
    answer=int(input("1.查询，2.添加，3.删除，4.修改,5.退出:"))

    #退出
    if answer==5:
        break
    
    elif answer==1:
        #查询
        person=input("请输入通讯人：")
        print(person+"的电话号码是"+str(smartphones[person]))
        answer=input("你是否想要拨打此号码(y/n):")

        #拨打
        if answer=="y":
            print("拨号中……")
            time.sleep(10)
            print("对不起，您拨打的号码暂时无法拨通，请稍候再拨……")
            continue
    
    #添加
    elif answer==2:
        person=input("请输入通讯人：")
        phone=int(input("请输入电话号码："))
        smartphones[person]=phone
        print("添加成功")
        print(smartphones)
        
    #删除
    elif answer==3:
        person=input("请输入通讯人：")
        answer=input("【WARNING】:你确定要删除通讯人"+person+"(y/n):")
        if answer=="y":
            del smartphones[person]
            print("删除成功")
            print(smartphones)
        else:
            print("未删除")
    
    #修改
    elif answer==4:
        person=input("请输入通讯人：")
        phone=int(input("请输入新的电话号码："))
        smartphones[person]=phone
        print("修改成功")
        print(smartphones)
    
    #出错
    else:
        print("出错！"*10)
