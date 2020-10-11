import smtplib
from email.mime.text import MIMEText


def send_email(email,mesmage):
    host = 'smtp.qq.com'
    port = 25
    msg = MIMEText(mesmage, "html")
    # msg['subject'] = "给您发送了注册信息"
    # msg["from"] = "xj-ie"
    # msg['to'] = email
    s = smtplib.SMTP(host, port)
    s.login("839987194@qq.com","gyftuygsvdgdbdgg")
    s.sendmail("839987194@qq.com", email, msg.as_string())


if __name__ == '__main__':
    send_email("3224218406@qq.com","qpwq")

