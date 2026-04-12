"""This module parse the response provide by the fecther to return the title,
the price, the availability and the rating of the books in the current scrape
page"""

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

    def parse_title(self) -> str:
        """
        Parse the title of the book
        """
        
