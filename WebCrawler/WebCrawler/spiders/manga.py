import scrapy
from WebCrawler.pipelines import *
from scrapy import Request
from WebCrawler.items import ReviewsMangaItem

class MangaSpider(scrapy.Spider):
    name = "manga"
    allowed_domains = ["myanimelist.net"]
    start_urls = [f"https://myanimelist.net/manga.php?letter={i}" for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W','X', 'Y', 'Z'] ]

    database = DataBase('manga')

    try:
       database.create_table('manga', title = db.String, img = db.String, desc = db.String, page = db.String)
    except:
         pass
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_manga)

    def parse_manga(self, response):
        liste_manga = response.css('div.js-categories-seasonal tr')[1:]


        for manga in liste_manga:
            item = ReviewsMangaItem()

            #titre du manga

            try:
                item['title'] = manga.css('strong::text').get()
            except:
                item['title'] = 'None'

            #image du manga

            try:
                item['img'] = manga.css('img::attr(data-src)').get()
            except:
                item['img'] = 'None'

            #description du manga

            try:
                item['desc'] = manga.css('div.pt4::text').get()
            except:
                item['desc'] = 'None'

            #page du manga

            try:
                item['page'] = response.css('a.horiznav_active::text').get()
            except:
                item['page'] = 'None'


            self.database.add_row('manga', title = item['title'], img = item['img'], desc = item['desc'], page = item['page'])

            yield item


