import time
from pygame import mixer
mixer.init()
hour = int(input('请输入____小时:'))
minute = int(input('请输入____分钟:'))
second = int(input('请输入____秒:'))
goal = hour*60*60+minute*60+second
music_time = int(input('请输入音乐播放时间(s)：'))
past = time.time()
while 1:
    now = time.time()
    time_ = now - past
    if time_ >= goal-1 and time_ <= goal+1:
        print('时间到')
        mixer.music.load('C:\shockley\我的\音乐\纯音乐 - Canon In D Major (钢琴).mp3')
        mixer.music.play()
        time.sleep(music_time)
        break
    else:
        pass
