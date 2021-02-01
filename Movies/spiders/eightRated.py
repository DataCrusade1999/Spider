import scrapy


class MoviesSpider(scrapy.Spider):
    name = "movieCrawler"

    #def start_requests(self):
    start_urls = [
            'https://yts.mx/browse-movies/0/all/all/8/latest/0/all?page=2',
            'https://yts.mx/browse-movies/0/all/all/8/latest/0/all?page=3'
        ]
        #for url in urls:
        #    yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for movies in response.xpath('//div[@class="browse-movie-bottom"]/a/text()').getall():
            with open('Movies.txt','w') as f:
                f.write(movies)

    
