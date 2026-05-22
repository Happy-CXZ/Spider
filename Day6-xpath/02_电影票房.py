from lxml import etree

f = open("电影票房.html","r",encoding="utf-8")
code = f.read()
f.close()

page = etree.HTML(code)

movie_list = page.xpath("//table/tbody/tr")[1:][:-6]
for movie in movie_list:
    year = movie.xpath("td[2]/text()")[0]
    name = movie.xpath("td[3]/text()")[0]
    money = movie.xpath("td[4]/text()")[0]
    print(year, name, money)

# years = page.xpath("//table/tbody/tr/td[2]/text()")
# names = page.xpath("//table/tbody/tr/td[3]/text()")
# moneys = page.xpath("//table/tbody/tr/td[4]/text()")
# for year, name, money in zip(years, names, moneys):
#     print(year,name,money)