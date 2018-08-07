from urllib.request import  urlopen
from  bs4 import BeautifulSoup

path = 'X:\Python source code\weather\\temp.txt'
html = urlopen('https://weather.com/weather/today/l/37.42,-121.90').read().decode('utf-8')

s = BeautifulSoup(html, features='html.parser')

local_time = s.find_all('p', {'class' : 'today_nowcard-timestamp'})
for lt in local_time:
    local_time = lt.get_text()
temperature = s.find_all('div', {'class' : 'today_nowcard-temp'})
for t in temperature:
    temperature = t.get_text()
weather = s.find_all('div', {'class' : 'today_nowcard-phrase'})
for w in weather:
    weather = w.get_text()
feels_like = s.find_all('span', {'class' : 'deg-feels'})
for fl in feels_like:
    feels_like = fl.get_text()

print ('\n', local_time )
print ('\n', temperature)
print ('\n', weather)
print ('\n', feels_like)

