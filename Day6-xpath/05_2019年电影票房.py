from lxml import etree
import requests
from bs4 import BeautifulSoup

url = "http://www.boxofficecn.com/boxoffice2019"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36'
}

response = requests.get(url,headers=headers)

tree = etree.HTML(response.text)
f = open("movie.txt","w",encoding="utf-8")

movie_list = tree.xpath("//table/tbody/tr")[1:-1]
for movie in movie_list:
    num = movie.xpath("./td[1]/text()")[0]
    year = movie.xpath("./td[2]//text()")[0]
    name = movie.xpath("./td[3]//text()")[0]
    money = movie.xpath("./td[4]/text()")[0]
    f.write(f'{num}\t{year}\t{name}\t{money}\n')
f.close()