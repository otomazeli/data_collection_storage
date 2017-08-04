import scrapy
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from ..items import GamesofthronesItem


class redditScrapper(CrawlSpider):
    # spider name
    name = 'redditscrapper'
    # list of allowed domains
    allowed_domains = ['reddit.com']
    # staring url for scraping
    start_urls = ['https://www.reddit.com/r/gameofthrones/']
    # location of csv file
    # custom_settings = {
    #     'FEED_URI': 'tmp/reddit.csv'
    # }


    rules =(Rule(LinkExtractor(allow=(), restrict_css=(".next-button",)), callback="parse_pages", follow=True),)

    def parse_pages(self, response):

        titles = response.css('.title.may-blank::text').extract()
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()
        items = []

        for item in zip(titles, votes, times, comments):
            print("In loop")
            itemz = GamesofthronesItem()
            itemz['Title'] = item[0]
            itemz['Vote'] = item[1]
            itemz['Created_at'] = item[2]
            itemz['Comments'] = item[3]
            items.append(itemz)
        return items
