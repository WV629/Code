import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_qq_email(sender_email, sender_password, receiver_email, subject, content):
    # QQ邮箱的SMTP服务器地址和端口号
    smtp_server = 'smtp.qq.com'
    smtp_port = 465

    # 发送方的邮箱账号和密码
    sender_email = sender_email
    sender_password = sender_password

    # 接收方的邮箱账号
    receiver_email = receiver_email

    # 构造邮件内容
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    try:
        # 创建SMTP对象，连接到QQ邮箱的SMTP服务器，并启用SSL加密连接
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)

        # 发送邮件
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # 关闭连接
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败:", e)

# 使用示例：
if __name__ == "__main__":
    sender_email = "2762882807@qq.com"
    sender_password = "luftjoescukfddbi"
    receiver_email = "2762882807@qq.com"
    subject = "测试邮件"
    content = "这是一封测试邮件，用于测试发送QQ邮件的方法。"
    send_qq_email(sender_email, sender_password, receiver_email, subject, content)
