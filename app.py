from seleniumrequestshtml import Chrome
from selenium.webdriver.chrome.options import Options

url = 'https://illsea.com'
options = Options()
options.add_argument("--headless")
webdriver = Chrome(chrome_options=options)

session = webdriver.requests_session
response = session.get(url)

images = response.html.find('img')

print(images)