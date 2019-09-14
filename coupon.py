import requests
from pyquery import PyQuery as pq


class Coupon:
    def __init__(self):
        pass

    def start(self):
        # 自营
        # self.coupon("https://search.jd.com/Search?coupon_batch=250384466&coupon_id=41554084423")

        # 自营+第三方
        self.coupon("https://search.jd.com/Search?coupon_batch=246420694&coupon_id=40951182275")

    def coupon(self, url):
        sess = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        i = 1
        while True:
            newurl = '{}&page={}&scrolling=y'.format(url, i)
            res = sess.get(url=newurl, headers=headers)
            res.encoding = 'utf-8'
            data = self.parse(res.text)
            if len(data) == 0:
                return
            # print(newurl, len(data))
            i = i + 1

    def parse(self, html):
        doc = pq(html)
        items = doc.find(".gl-item").items()
        datas = {}
        for item in items:
            title = item.find(".p-name em").text()
            url = "https:" + item.find(".p-img a").attr("href")
            price = item.find(".p-price").text()
            shop = item.find(".p-shop").text()
            one_data = {
                "title": title,
                "url": url,
                "price": price,
                "shop": shop,
            }
            # print(one_data)
            datas[url] = one_data

        return datas


if __name__ == "__main__":
    c = Coupon()
    c.start()
