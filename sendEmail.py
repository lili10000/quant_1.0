#-*-coding:utf-8-*-
import smtplib
import time
from email.mime.text import MIMEText

def sendMailToMe(info):
    _user = "476512727@qq.com"
    _pwd  = "wespnvdsxsofcadc"
    _to   = "476512727@qq.com"

    msg = MIMEText(info)
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    msg["Subject"] = "[量化建议]" + today
    msg["From"]    = _user
    msg["To"]      = _to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "Success!"
    except smtplib.SMTPException,e:
        print "Falied,%s"%e 

