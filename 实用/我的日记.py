#定义写日记函数
def write_diary():
    import time
    str_diary="\n"
    now=time.asctime(time.localtime())
    str_diary+=now
    str_diary+="\n---------------------\n"
    title=input("请输入标题：")
    str_diary+="《"+title+"》"
    print(str_diary)
    print("(请输入日记，输入end并回车结束）")
    line=""
    while line != "end":
        line=input()
        str_diary+="\n"+line
    return str_diary+"\n"
#end def

answer=int(input("写入请摁1，读取请摁2："))
file_name="C:/shockley/我的/编程/实用/我的日记.txt"

#获取信息
print("文件名："+file_name)
#写入日记
if answer==1:
    fo=open(file_name,'a',encoding="utf-8")
    new_diary=write_diary()
    fo.write(new_diary)
    print("写入成功！")

#读取日记
if answer==2:
    fo=open(file_name,'r',encoding="utf-8")
    all_diary=fo.read()
    print(all_diary)
fo.close()
