# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


def clean_price(text: str):
    return text.strip('€'' ').replace('.', '')


class HouseItem(Item):
    title = Field(
        output_processor=TakeFirst())
    price =Field(
        input_processor=MapCompose(clean_price),
        output_processor=TakeFirst()
    )
    location = Field(
        output_processor=TakeFirst()
    )
