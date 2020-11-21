number=int(input("请输入数字:"))
times=0
jurges=1
if number>0:
    for x in range(number):
        if number%jurges==0:
            times+=1
            jurges+=1
        else:
            jurges+=1
else:
    number=-number
    for x in range(number):
        if number%jurges==0:
            times+=1
            jurges+=1
        else:
            jurges+=1
if times==2:
    print(str(number)+"是一个素数.")
else:
    print(str(number)+"不是一个素数.")
