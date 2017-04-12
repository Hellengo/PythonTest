# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

def sendMail(text):
    sender = 'hailong.gao@speedx.com'
    receiver = ['hailong.gao@speedx.com']
    subject = '[AutomantionTest]接口自动化测试报告通知'
    smtpserver = 'smtp.office365.com'
    username = 'hailong.gao@speedx.com'
    password = 'newton-123'

    msg = MIMEText(text, 'html', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ';'.join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 587)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver , msg.as_string())
    smtp.quit()


def main():
        html = '<html><body>接口自动化扫描，共有 ' + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;">接口</th><th style="width:50px;">状态</th><th style="width:200px;">接口地址</th><th>接口返回值</th></tr>'
        print "--------sending email-------"
        sendMail(html)
        print "--------sent email----------"

if __name__ == '__main__':
    main()
