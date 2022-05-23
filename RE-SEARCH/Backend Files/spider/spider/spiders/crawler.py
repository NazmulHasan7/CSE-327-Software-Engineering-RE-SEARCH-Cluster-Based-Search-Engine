# import itemloaders
from scrapy import spiders
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from crawl.items import SpideyItem
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging



class crawler(CrawlSpider):
    name = 'spidey'
    start_urls = []

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    
    
    def parse_item(self, response):

        item = dict()
        item['url'] = response.url.strip()
        item['title'] = response.meta['link_text'].strip()
        # extracting basic body
        #item['body'] = '\n'.join(response.xpath('normalize-space(.//text())').extract())
        item['body'] = '\n'.join(response.xpath(
            './/text()').extract())
        # or better just save whole source
        #item['source'] = response.body

        yield item

def begin_crawl(link, height, id):

    configure_logging()
    runner = CrawlerRunner(settings={
    "DEPTH_PRIORITY" : 1,
    'DEPTH_LIMIT': height,
    'SCHEDULER_DISK_QUEUE' : 'scrapy.squeues.PickleFifoDiskQueue',
    'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue',
    
    })
    runner.crawl(crawler, start_urls=[link], depth= height)
    
    #runner.crawl(MySpider2)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers= False)  # the script will block here until all crawling jobs are finished
    #reactor.stop()
    print('successful!!!')
    print('successful!!!')
    
    
    
    