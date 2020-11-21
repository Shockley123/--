#猜
import random
times=0
answer=input("想玩吗？(如果不玩，请回车）:")
while answer!="":
    number=random.randint(1,100)
    guess=int(input("猜一个数字(1~100):"))
    while guess !=number:
        times=times+1
        if guess<number:
            print("太小")
        if guess>number:
            print("太大")
        guess=int(input("再猜一个数字:"))
    times=times+1
    print(guess,"是对的!你用了",times,"次")
    times=0
    answer=input("想玩吗？(如果不玩，请回车）:")
print("欢迎下次来玩！")
