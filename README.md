Selenium Requests HTML
=================
Extends Selenium WebDriver classes to include the [HTMLSession](http://html.python-requests.org/) from the [Requests-HTML](http://html.python-requests.org/) library, while doing all the needed cookie and request headers handling.

This hasn't really been tested and is not likely to get a whole lot of work done on it. My initial tests seemed to work for my use case. Most functionality worked with another webdriver, but the render function in Requests-HTML has a dependency that uses chromedriver and I have not yet looked into a way around it.

Most of the work already seemed to have been done, thanks to the organization and work already done in [Selenium Requests](https://github.com/cryzed/Selenium-Requests) and [Requests-HTML](http://html.python-requests.org/), as well as the original [Requests](http://python-requests.org/) library.

Usage
-----
```python
# Import any WebDriver class that you would usually import from
# selenium.webdriver from the seleniumrequestshtml module
from seleniumrequestshtml import Chrome
from selenium.webdriver.chrome.options import Options

# Set up the options for your webdriver
url = 'https://illsea.com'
options = Options()
options.add_argument("--headless")
webdriver = Chrome(chrome_options=options)

# webdriver.requests_session replaces regular HTMLSession() usage from requests-html
session = webdriver.requests_session
# Then just do requests-HTML stuff like so
response = session.get(url)
images = response.html.find('img')

print(images)

# Installing

pip install selenium-requests-html

