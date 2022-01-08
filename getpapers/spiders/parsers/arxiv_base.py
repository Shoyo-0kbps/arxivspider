import scrapy
from scrapy.loader import ItemLoader
from getpapers.spiders.items import ArxivscraperItem
<<<<<<< HEAD

=======
>>>>>>> GRP-1-IO-base

class ArxivSpider(scrapy.Spider):
    name = "arxiv_base"

    start_urls = ["https://arxiv.org/"]

    def parse(self, response):

        for topics in response.xpath(
            '//div[contains(@id,"content")]//ul[preceding-sibling::h2]//li'
        )[:-5]:

            l = ItemLoader(item=ArxivscraperItem(), selector=topics)
            latest_loader = l.nested_xpath(
                ".//a[position() >= 2 and (position() <= 3)]"
            )
            l.add_xpath("category_name", ".//a")
            latest_loader.add_xpath("latest_name", ".")
            latest_loader.add_xpath("latest_link", "./@href")
            l.add_xpath(
                "subcategory_name",
                './/a[preceding-sibling::br and not(text()="detailed description")]',
            )
            l.add_xpath(
                "subcategory_link",
                './/a[preceding-sibling::br]/@href[not(contains(.,"help"))]',
            )

            yield l.load_item()
