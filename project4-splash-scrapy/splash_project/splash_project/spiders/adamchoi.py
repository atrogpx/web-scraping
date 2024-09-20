import scrapy
from scrapy_splash import SplashRequest


class AdamchoiSpider(scrapy.Spider):
    name = "adamchoi"
    allowed_domains = ["www.adamchoi.co.uk", "localhost"]
    # start_urls = ["https://www.adamchoi.co.uk"]

    script = '''
        function main(splash, args)
                -- If a website doesn't render correctly, disabling Private mode might help
            splash.private_mode_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(3))
            buttons = assert(splash:select_all('label.btn-primary'))
            buttons[2]:mouse_click()
            assert(splash:wait(3))
                -- Increase the viewport to make all the content visible
            splash:set_viewport_full()
            return {splash:png(), splash:html()}
        end
    '''
    def start_requests(self):
        yield SplashRequest(url='https://www.adamchoi.co.uk/overs/detailed', callback=self.parse,
                            endpoint='execute', args={'lua_source': self.script, 'output_format': 'html'})

    def parse(self, response):
        rows = response.xpath('//tr')

        for row in rows:
            date = row.xpath('./td[1]/text()').get()
            home_team = row.xpath('./td[2]/text()').get()
            score = row.xpath('./td[3]/text()').get()
            away_team = row.xpath('./td[4]/text()').get()
            yield {
                'date': date,
                'home_team': home_team,
                'score': score,
                'away_team': away_team
            }
