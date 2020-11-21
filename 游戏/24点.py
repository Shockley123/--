#24点游戏
import random
import time
answer=input("大家好！想玩24点吗？(y/n):")
while answer=="y":
    print("发牌中……")
    print("第1张：a=",random.randint(1,13))
    time.sleep(1)
    print("第2张：b=",random.randint(1,13))
    time.sleep(1)
    print("第3张：c=",random.randint(1,13))
    time.sleep(1)
    print("第4张：d=",random.randint(1,13))
    time.sleep(1)
    e=eval(input("请输入算式:"))
    while e !=24:
        print("不对！请再输一次.")
        e=eval(input("请输入算式:"))
    print("你赢了！恭喜你！")
    answer=input("大家好！想玩24点吗？(y/n):")
print("欢迎下次来玩。")
