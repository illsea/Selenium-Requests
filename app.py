from seleniumrequestshtml import Chrome
from selenium.webdriver.chrome.options import Options

url = 'https://illsea.com'
options = Options()
options.add_argument("--headless")
webdriver = Chrome(chrome_options=options)
response = webdriver.requests_session.get(url)
links = response.html.links
images = response.html.find('img')
absolute_links = response.html.absolute_links

print(images)