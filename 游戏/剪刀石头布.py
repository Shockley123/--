#剪刀石头布
import random
import time
choice=["石头","剪刀","布"]
keep_going=True
while keep_going:
    #选择
    print("请准备游戏开始。")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    your=input("请选择剪刀，石头或布:")
    computer=random.choice(choice)
    print("你选择了"+your+"而电脑选择了"+computer)
    time.sleep(1)
    #判断胜负
    if your==computer:
        print("平局")
    elif your=="石头":
        if computer=="布":
            print("电脑赢了")
        else:
            print("你赢了")
    elif your=="剪刀":
        if computer=="石头":
            print("电脑赢了")
        else:
            print("你赢了")
    elif your=="布":
        if computer=="剪刀":
            print("电脑赢了")
        else:
            print("你赢了")
    else:
        print("出错了")
    keep_going=(input("想玩吗？如果不想，请摁回车键:")!="")
            
