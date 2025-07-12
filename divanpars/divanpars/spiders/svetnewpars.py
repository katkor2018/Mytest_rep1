import scrapy

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):
        # Выведет статус-код запроса
        print(f"Status code: {response.status}")

        divans = response.css('div._Ud0k')
        for divan in divans:
            name = divan.css('span[itemprop="name"]::text').get()
            price = divan.css('span[data-testid="price"]::text').getall()
            url = response.urljoin(divan.css('a::attr(href)').get())
            print(f"Name: {name}\nPrice: {price}\nURL: {url}\n")
            yield {
                'name': name,
                'price': price,
                'url': url
            }

