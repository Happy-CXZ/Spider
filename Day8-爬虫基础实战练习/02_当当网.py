"""
网址:https://category.dangdang.com/cp01.01.02.00.00.00.html
目标:商品的标题，价格，标签，简介
"""
import requests
from lxml import etree


def get_one_page_data(url,file):
    # url = 'https://category.dangdang.com/cp01.01.02.00.00.00.html'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "connection": "keep-alive",
        "cookie": "__permanent_id=20260609181005542213642604271440976; acw_tc=0a43edb217811581535856313e3c2825b385fc47dd83b6fdbcc86afdd9fae2; search_passback=277100891a762cd209512a6a000000003920660008512a6a; ddscreen=2; __visit_id=20260611140912901400006509415504782; __out_refer=; __trace_id=20260611140912902406673788171404836; pos_6_start=1781158153049; pos_9_end=1781158153152; ad_ids=109519062%7C%231; pos_6_end=1781158154219",
        "host": "category.dangdang.com",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "cross-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    page = etree.HTML(response.text)
    books = page.xpath(".//div[@id='search_nature_rg']/ul/li")
    # print(len(books))

    for book in books:
        # 标题
        title = "".join(book.xpath(".//p[@name='title']/a/text()")).strip()
        # print(title)
        # 价格：当前价格、定价
        # 有的价格格式是xxx起
        now_price = "".join(book.xpath(".//span[@class='search_now_price']//text()")).strip()
        if "-" in now_price:
            now_price = now_price.split("-")[0].strip() + "起"
        pre_price = "".join(book.xpath(".//span[@class='search_pre_price']/text()"))
        if not pre_price:
            pre_price = "-"
        # print(now_price,pre_price)
        # 标签
        book_author = "".join(book.xpath(".//p[@class='search_book_author']//text()")).strip()
        # print(book_author)
        author = "".join(book.xpath(".//p[@class='search_book_author']/span[1]//text()")).strip().replace("/", "").replace(",", "，")
        year = "".join(book.xpath(".//p[@class='search_book_author']/span[2]//text()")).strip().replace("/", "").replace(",", "，")
        publisher = "".join(book.xpath(".//p[@class='search_book_author']/span[3]//text()")).strip().replace("/", "").replace(",", "，")
        # print(author,year,publisher)
        # 简介
        detail = "".join(book.xpath(".//p[@class='detail']//text()"))
        # print(detail)
        s = f'{title},{now_price},{pre_price},{author},{year},{publisher},{detail}\n'
        # s = f'{title},{now_price},{pre_price},{book_author},{detail}\n'
        file.write(s)


def main():
    with open("books.csv", "w", encoding="utf-8") as f:
        for i in range(1, 2):
            if i == 1:
                url = "https://category.dangdang.com/cp01.01.02.00.00.00.html"
            else:
                url = f"https://category.dangdang.com/pg{i}-cp01.01.02.00.00.00.html"
            get_one_page_data(url,f)
            print(f"第{i}页保存完毕")
if __name__ == '__main__':
    main()