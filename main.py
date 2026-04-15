"""Orchestrator module"""

from scraper import fetcher, parser, exporter, utils
from requests.exceptions import HTTPError


def request_generator(url: str):
    """
    Request generator
    
    :param url: URL (base) to request
    :type url: str
    """
    i = 1
    while True:
        try:
            response = fetcher.Fetcher(f"{url}/catalogue/page-{i}.html") # Instance of fetcher Object
            yield response.make_request() # Lazy evaluation of response 
            i += 1
        except HTTPError: # Catch the 404 error
            return # End properly the generator

@utils.timer
def main():
    """Main function to orchestrate the scraping"""
    products = []
    for response in request_generator("https://books.toscrape.com"):
        parse_response = parser.Parser(response).get_products()
        products.extend(parse_response)
    
    files = exporter.Exporter(products)
    files.to_csv("books_scrape.csv")
    files.to_json("books_scrape.json")


if __name__ == "__main__":
    """Execute the script."""
    main()

