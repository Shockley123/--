#电子邮件
#使用utf-8
#coding:utf-8
#导入模块
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

#发邮件函数
def sent():

    #我的邮箱
    my_mail='sxxx20153405@163.com'
    my_password = 'BJTJBJDAZOSAJIFL'

    #对方邮箱
    your_mail=input('收件人：')

    #主题
    theme=input('主题：')

    #正文
    print('正文：')
    email_text='    '
    for line in iter(input,''):
        email_text += line+'\n'

    #发送
    keep_going=True
    try:
        msg=MIMEText(email_text,'plain','utf-8')
        msg['From']=formataddr(['发件人',my_mail])
        msg['To']=formataddr(['收件人',your_mail])
        msg['Subject']=theme

        server=smtplib.SMTP('smtp.163.com',25)
        server.login(my_mail,my_password)
        server.sendmail(my_mail,[your_mail,],msg.as_string())
        server.quit()
    except BaseException as mye:
        keep_going=False
        print('error='+format(mye))
    return keep_going

#发送
ret=sent()
if ret:
    print('Email is sent successfully.')
else:
    print('Fail to send.')
