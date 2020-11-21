number=1
range_input=int(input("请输入范围(最大值):"))
jurge=1
times=0
while number<=range_input:
    for x in range(number):
        if number%jurge==0:
            times+=1
            jurge+=1
        else:
            jurge+=1
    if times==2:
        print(str(number),end=" ")
    number+=1
    times=0
    jurge=1
