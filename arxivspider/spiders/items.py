import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


class ArxivscraperItem(scrapy.Item):

    category_name = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    latest_name = scrapy.Field(input_processor=MapCompose(remove_tags))
    latest_link = scrapy.Field()
    subcategory_name = scrapy.Field(input_processor=MapCompose(remove_tags))
    subcategory_link = scrapy.Field()
