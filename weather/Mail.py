import smtplib
from email.message import EmailMessage

Sender = "278627159@qq.com"     # 发件人Email地址

AuthorizationCode = 'cwaveixscvjmcaci'       # 授权码，163邮箱开启SMTP服务时授权第三方登陆邮箱的授权码

receiver = "tcgkw1986@gmail.com"       # 收件人地址

smtp_server = 'smtp.qq.com'             # SMTP服务器地址

msg = EmailMessage()

msg.set_content('你好！我是Python发邮测试！', 'plain', 'utf-8')       # 邮件正文

msg['Subject'] = '测试'    # 邮件主题

msg['From'] = Sender   # 发件人，显示在收件人界面上

msg['To'] = receiver     # 收件人

smtpObj = smtplib.SMTP_SSL(smtp_server, 465)     # 465 为 SMTP  SSL 端口号


smtpObj.login(Sender, AuthorizationCode)      # 登陆邮箱

smtpObj.sendmail(Sender, receiver, msg.as_string())   # 发送邮件

smtpObj.quit()    # 推出
