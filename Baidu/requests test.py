import requests
# from requests import requests.get
import webbrowser

param = {'wd': 'Python'}
r = requests.get('http://www.baidu.com/s', params = param)
print(r.url)
# webbrowser.open(r.url)

data = {'firstname': 'RUA', 'lastname': 'Zhuang'}
r2 = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r2.text)

# payload = {'username': 'RUA', 'password': 'password'}
# r = requests.session().post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
#
# r = requests.session().get("http://pythonscraping.com/pages/cookies/profile.php")
# print(r.text)


session = requests.Session()
payload = {'username': 'RUA', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# {'username': 'Morvan', 'loggedin': '1'}


r = session.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)