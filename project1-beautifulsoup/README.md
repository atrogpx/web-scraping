The first project of the course "Web Scraping in Python Selenium, Scrapy + ChatGPT Prize 2024" by Frank Andrade.
https://www.udemy.com/course/web-scraping-course-in-python-bs4-selenium-and-scrapy/

In part one of this project we extract scripts from the url mentioned in the code (using BeautifulSoup) and write each of them in a seperate text file.

Some code explanation:

Fetch the pages
result=requests.get("www.google.com")
result.status_code # get status code
 result.headers # get the headers

 Page content
 content = result.text
 
 Create Soup
 soup = BeautifulSoup(content,"lxml")

 Get inner text
 sample = element.get_text(strip=True, separator= ' ')

Get specific attributes
sample = element.get('href')

In the second part of this project we scrape the rest of the pages of the website using pagination. Also try/except is used so that if a link was broken, the whole process and the code doesn't break.
