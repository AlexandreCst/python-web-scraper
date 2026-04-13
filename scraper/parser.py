"""This module parse the response provide by the fecther to return the title,
the price, the availability and the rating of the books in the current scrape
page"""

from bs4 import BeautifulSoup
import requests

class Parser:
    """
    Parser class
    """
    def __init__(self, response: str):
        """
        Constructor initialisation
        
        :param response: Response of the requests provides by fetcher
        :type response: str
        """
        self.response = response

    def parse_title(self) -> list[str]:
        """
        Parse the title of the book
        """
        articles = self._get_article()
        titles = [article.find("h3").a["title"] for article in articles]
        return titles

    def _get_article(self) -> list[str]:
        """
        Private method to build the soup object and get the article
        
        :param self: Description
        """
        soup = BeautifulSoup(self.response, "html.parser")
        articles = soup.find_all("article", class_="product_pod")
        return articles
