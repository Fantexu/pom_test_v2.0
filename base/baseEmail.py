import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_report(report_path):
    report_list = os.listdir(report_path)
    report_list.sort(key=lambda report: os.path.getmtime(os.path.join(report_path, report)))
    return os.path.join(report_path, report_list[-1])


def send_email(report_path, sender, pwd, recevier, server, port=0):
    with open(get_report(report_path), 'rb') as file:
        mail_body = file.read()

    msg = MIMEMultipart()
    msg['Subject'] = '{}_用例报告'.format(time.strftime('%Y_%m_%d %H_%M_%S'))
    msg['from'] = sender
    msg['to'] = ';'.join(recevier)

    body = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(body)

    # 上传附件
    accessory = MIMEText(mail_body, 'base64', 'utf-8')
    accessory['Content-Type'] = 'application/octet-stream'
    accessory['Content-Disposition'] = 'attachment; filename= "result.html"'
    msg.attach(accessory)

    try:
        smtp = smtplib.SMTP()
        smtp.connect(server)
    except:
        smtp = smtplib.SMTP_SSL(server, port)

    smtp.login(sender, pwd)
    smtp.sendmail(sender, recevier, msg.as_string())
    smtp.quit()
    print('邮件发送成功')