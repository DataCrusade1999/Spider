import scrapy


class MoviesSpider(scrapy.Spider):
    name = "movieCrawler"

    start_urls = [
            'https://yts.mx/browse-movies/0/all/all/8/latest/0/all'
            
        ]
 
    
    def parse(self, response):
        for movies in response.css('.browse-movie-bottom>a::text').getall():
            with open('Movies.txt','a') as f:
                f.write(f'{movies}\n')
          

        for i in range(2,44):
            next_page = 'https://yts.mx/browse-movies/0/all/all/8/latest/0/all?page=' + str(i)
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
        
