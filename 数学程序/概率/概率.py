# 随机
# 导入模块
import random
import time

# 设置
lists = range(1,3)
lists = list(lists)
keep_going = True
times_1 = 0
times = int(input('请输入次数:'))
time_1 = time.time()

# 实验
for x in range(1,times):
    good = random.choice(lists)
    if good == 1:
        times_1 += 1

# 计算概率
time_2 = time.time()
time_all = time_2-time_1
possible = times_1/times
print('频率:',possible)
print('时间:',time_all)
print('概率:',1/len(lists))
print('误差:',abs(1/len(lists)-possible))
