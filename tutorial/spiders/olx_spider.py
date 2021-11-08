import scrapy
from tutorial.items import HouseItem
from scrapy.loader import ItemLoader

class OlxSpider(scrapy.Spider):
    
    name = "houses"

    start_urls = ['https://www.olx.pt/imoveis/apartamento-casa-a-venda/apartamentos-venda/porto/']

    def parse(self, response):
        self.logger.info("Spider test")
        houses = response.css('div.offer-wrapper')
        for house in houses:
            loader = ItemLoader(item=HouseItem(),selector=house)
            loader.add_css('title', 'a.marginright5.link.linkWithHash.detailsLink strong::text')
            loader.add_css('price', 'p.price strong::text')
            
            house_item = loader.load_item()

            house_url = house.css('a::attr(href)').get()
            if 'imovirtual' in house_url:
                yield response.follow(house_url, callback=self.parse_imovirtual_url, meta={'house_item': house_item})
            else:
                ##yield response.follow(house_url, callback=self.parse_olx_url)
                self.logger.info('Not implemented')
            
        next_page = response.css('span.fbold.next.abs.large a::attr(href)').get()
        print (f'proxima pagina {next_page}')
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
        
        
    def parse_imovirtual_url(self, response):
        house_item = response.meta['house_item']
        loader = ItemLoader(item=house_item,response= response)
        loader.add_css('location', 'a.e1nbpvi60.css-1ji3day.e1enecw71::text')
        yield loader.load_item()
        
#    def parse_olx_url(self, response):
#       yield {
#            'Test':'asd'
#            
#        }
