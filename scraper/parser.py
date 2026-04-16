"""This module parse the response provide by the fecther to return the title,
the price, the availability and the rating of the books in the current scrape
page"""

from bs4 import BeautifulSoup, Tag

from scraper.exceptions import EmptyListError
from scraper.utils import logger

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
        self.response = response # Request response
        self.articles = self._get_article() # Get the whole products of the page

    # Public methods - Parsing:
    def parse_title(self) -> list[str]:
        """
        Parse the title of the current page books and return the list of it
        
        :return: List of titles
        :rtype: list[str]
        """
        titles = [article.find("h3").a["title"] for article in self.articles] # List of the titles
        return titles

    def parse_price(self) -> list[float]:
        """
        Parse the price of the current page books and return the list of it
        
        :return: List of prices
        :rtype: list[float]
        """
        prices = [float(self._extract_price(article)) for article in self.articles] # List of float converted prices
        return prices
    
    def parse_availability(self) -> list[str]:
        """
        Parse the availability of the current page books and return the list of 
        it
        
        :return: List of availabilities
        :rtype: list[str]
        """
        availabilities = [self._extract_availability(article) for article in self.articles] # List of books availabilities
        return availabilities
    
    def parse_rating(self) -> list[str]:
        """
        Parse the rating of the current page books and return the list of 
        it
        
        :return: List of ratings
        :rtype: list[str]
        """
        ratings = [self._extract_rating(article) for article in self.articles] # List of books rating
        return ratings
    
    # Public method - Parsing orchestration:
    def get_products(self) -> list[dict[str, str | float]]:
        """
        Method to orchestrate the whole parsing
        
        :return: List of dict with title, price, availability and rate for each book
        :rtype: list[dict[str, str | float]]
        """
        title = self.parse_title()
        price = self.parse_price()
        availability = self.parse_availability()
        rate = self.parse_rating()

        # Make a list of dict that resume all books (title, price, ...) 
        products = [self._build_product(product) for product in zip(title, price, availability, rate)]
        return products


    # Private methods/functions
    def _get_article(self) -> list[str]:
        """
        Private method to build the soup object and get the article
        
        :param self: Description
        """
        soup = BeautifulSoup(self.response, "html.parser") # BeautifulSoup object
        articles = soup.find_all("article", class_="product_pod") # Get the balise about articles
        if not articles: # Raise an exception if no articles found
            logger.error(f"No articles found")
            raise EmptyListError("No articles found")
        logger.debug("Success, articles found!")
        return articles
    
    def _extract_price(self, article: Tag) -> str:
        """
        Private function to format the price of the article
        """
        return article.find("div", class_="product_price").p.get_text(strip=True).replace("£", "")
    
    def _extract_availability(self, article: Tag) -> str:
        """
        Private function to format the availability of the article
        """
        return article.find("p", class_="instock availability").get_text(strip=True)
    
    def _extract_rating(self, article: Tag) -> str:
        """
        Private function to format the rating of the article 
        """
        return article.find("p", class_="star-rating").get_attribute_list("class")[1]
    
    def _build_product(self, product: tuple) -> dict[str, str | float]:
        """
        Private function to format the dict with title, price, availability and 
        rating of a book
        """
        return {
            "title": product[0],
            "price": product[1],
            "availability": product[2],
            "rating": product[3]
        }