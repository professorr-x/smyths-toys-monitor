import requests
from bs4 import BeautifulSoup
from discord import send_hook
from datetime import datetime
import random


pid = ['192247', '192012', '191259', '191430', '193053', '193054']


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}


def privateProxies():
  print('Converting Proxies')
  with open('proxies.txt') as f:
    file_content = f.read()
  file_rows = file_content.split('\n')
  for i in range(len(file_rows)):
    if ':' in file_rows[i]:
      tmp = file_rows[i]
      tmp = tmp.split(':')
      proxies = {'http': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/',
                 'https': 'http://' + tmp[2] + ':' + tmp[3] + '@' + tmp[0] + ':' + tmp[1] + '/'}
      proxyList.append(proxies)
      f.close()


proxyList = []
privateProxies()

while True:
    for i in range(len(pid)):
        proxy = random.choice(proxyList)
        url = "https://www.smythstoys.com/uk/en-gb/p/{}".format(pid[i])

        try:
            response = requests.get(url, headers=headers, proxies=proxy)
            soup = BeautifulSoup(response.text, 'html.parser')
            stock_status = soup.find('span', attrs={'name': 'js-stockStatusCode'}).get_text()
            price = soup.find('div', attrs={'class': 'price_tag'}).get_text().strip()
            product_title = soup.find('h1').get_text()

            try:
                image_url = soup.findAll('img')[2]['src']
            except:
                image_url = soup.findAll('img')[2]['data-src']

            if stock_status == 'inStock':
                print('[{}] Product InStock'.format(str(datetime.now())))
                send_hook(product_title, url, price, image_url)
            else:
                print('[{}] Product OOS'.format(str(datetime.now())))

        except ConnectionError:
            print("Connection Error")
        except TimeoutError:
            print("Timeout Error")
        except Exception as e:
            print(e)


