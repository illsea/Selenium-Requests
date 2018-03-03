Selenium Requests HTML
=================
Extends Selenium WebDriver classes to include the [HTMLSession](http://html.python-requests.org/) from the [Requests-HTML](http://html.python-requests.org/) library, while doing all the needed cookie and request headers handling.

This hasn't really been tested and is not likely to get a whole lot of work done on it. My initial tests seemed to work for my use case. Most functionality worked with another webdriver, but the render function in Requests-HTML has a dependency that uses chromedriver and I have not yet looked into a way around it.

Most of the work already seemed to have been done, thanks to the organization and work already done in [Selenium Requests]
(https://github.com/cryzed/Selenium-Requests) and [Requests-HTML](http://html.python-requests.org/), as well as the original [Requests](http://python-requests.org/) library.


Before the actual request is made, a local HTTP server is started that serves a single request made by the webdriver instance to get the "standard" HTTP request headers sent by this webdriver; these are cached (only happens once during its lifetime) and later used in conjunction with the Requests library to make the requests look identical to those that would have been sent by the webdriver. Cookies held by the webdriver instance are added to the request headers and those returned in a response automatically set for the webdriver instance.


Features
--------
 * Determines and sends the default HTTP headers (User-Agent etc.) for the chosen WebDriver
 * Manages cookies bidirectionally between requests and Selenium
 * Switches to already existing window handles or temporarily creates them to work with the webdriver's cookies when making a request
 * All operations preserve the original state of the WebDriver (active window handle and window handles)
 * Tested to work with Selenium (3.0.1) using Mozilla Firefox (49.0.2), Google Chrome (54.0.2840.71) and PhantomJS (2.1.1)


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
response = session.get(url)
images = response.html.find('img')

print(images)