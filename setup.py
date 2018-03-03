from setuptools import setup

try:
    import pypandoc
except ImportError:
    pypandoc = None

if pypandoc:
    long_description = pypandoc.convert('README.md', 'rst')
else:
    with open('README.md') as file:
        long_description = file.read()

setup(
    name='selenium-requests-html',
    version='1.0',
    description=(
        'Fork of selenium-requests that extends Selenium WebDriver classes to include the functionality '
        'from the Requests-HTML library, while doing all the needed cookie and '
        'request headers handling. Credit for most of what makes this work goes to'
        'to Chris Braun and his original work done on Selenium-Requests'
        'https://github.com/cryzed/Selenium-Requests'
    ),
    long_description=long_description,
    author='Sylas Aldridge',
    author_email='sylas@illsea.com',
    url='https://github.com/illsea/Selenium-Requests-HTML',
    packages=('seleniumrequestshtml',),
    install_requires=(
        'requests',
        'selenium',
        'six',
        'tldextract'
    ),
    license='MIT',
    python_requires='>=3.6',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
