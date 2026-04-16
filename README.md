# WEB SCRAPER

![GitHub repo size](https://img.shields.io/github/repo-size/AlexandreCst/python-web-scraper)
![GitHub contributors](https://img.shields.io/github/contributors/AlexandreCst/python-web-scraper)

Web scraper is a scraper that allows you to scrape the books in books.toscrape website.

This project is architectured in python package with a fetcher (make the requests), parser and exporter
to export the result in CSV or JSON file. We also have some extra modules like custom exceptions and utils
that containes custom logger and decorators. Overall the main orchestrate the fetching, parsing and exportation
of the articles get on the website.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the 3.9 version of Python or above
* You have a Windows, Mac or Linux machine
* You have read this README.

## Installing python-web-scraper

To install web scraper, follow these steps:

Linux and macOS:
```
git clone https://github.com/AlexandreCst/python-web-scraper.git
cd scraper
```

## Using the scraper

To use the web scraper, follow these steps:

```
pip install -r requirements.txt
python main.py
```

## Author

Alexandre COSTE

## License

This project uses the following license: MIT License.