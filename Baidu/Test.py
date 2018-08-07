from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = 'https://baike.baidu.com'

history = ['/item/%E6%9D%8E%E5%85%86%E6%B4%9B']

for i in range(20):
    url = base_url + history[-1]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='html.parser')
    print(soup.find('h1').get_text(), '    URL:', base_url + history[-1])

    t = soup.find_all('a',
                      {
                          'target': '_blank',
                          'href': re.compile("/item/(%.{2})+$")})

    # print(t)

    if len(t) != 0:
        temp = random.sample(t, 1)[0]['href']
        if temp not in history:
            history.append(temp)
        else:
            print('duplicated!')
            t.pop()
            # history.append(random.sample(t, 1)[0]['href'])


    else:
        print('non!!!!')
        history.pop()
    #     # no valid sub link found
    #     history.pop()  # 可以往回跳一个？

    # print(history)





