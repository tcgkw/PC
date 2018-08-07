from urllib.request import  urlopen
from  bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

def get_weatherinfo():
    html = urlopen('https://weather.com/weather/today/l/37.42,-121.90').read().decode('utf-8')
    s = BeautifulSoup(html, features='html.parser')

    local_time = s.find_all('p', {'class': 'today_nowcard-timestamp'})
    for lt in local_time:
        local_time = lt.get_text()
    temperature = s.find_all('div', {'class': 'today_nowcard-temp'})
    for t in temperature:
        temperature = t.get_text()
    weather = s.find_all('div', {'class': 'today_nowcard-phrase'})
    for w in weather:
        weather = w.get_text()
    feels_like = s.find_all('span', {'class': 'deg-feels'})
    for fl in feels_like:
        feels_like = fl.get_text()

    return local_time, temperature, weather, feels_like


def send_mail(t):
    local_time, temperature, weather, feels_like  = t
    str1 = 'Local time is ' + local_time + '\n' + 'Temperature is: ' + str(temperature) + '\n' + 'Weather is: ' + weather + '\n' + 'It feels like: ' + feels_like
    # print(str1, type(str1))
    Sender = "278627159@qq.com"  # 发件人Email地址
    AuthorizationCode = 'cwaveixscvjmcaci'  # 授权码，邮箱开启SMTP服务时授权第三方登陆邮箱的授权码
    receiver = "tcgkw1986@gmail.com"  # 收件人地址
    smtp_server = 'smtp.qq.com'  # SMTP服务器地址
    msg = EmailMessage()
    msg.set_content(str1, 'plain', 'utf-8')  # 邮件正文
    msg['Subject'] = '天气情况 :)'  # 邮件主题
    msg['From'] = Sender  # 发件人，显示在收件人界面上
    msg['To'] = receiver  # 收件人
    smtpObj = smtplib.SMTP_SSL(smtp_server, 465)  # 465 为 SMTP  SSL 端口号
    smtpObj.login(Sender, AuthorizationCode)  # 登陆邮箱
    smtpObj.sendmail(Sender, receiver, msg.as_string())  # 发送邮件
    smtpObj.quit()  # 退出

x = get_weatherinfo()
send_mail(x)
