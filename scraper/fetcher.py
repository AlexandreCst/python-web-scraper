"""This module allow to make a request and check if there is a success."""
from scraper.utils import retry, logger

import requests


class Fetcher:
    """Class to make some requests."""

    def __init__(self, url: str) -> None:
        """Constructor initialisation"""
        self.url = url

    @retry(n=3, delay=1)
    def make_request(self, timeout: float=1) -> str | None:
        """Make requests and handle by status code"""
        response = requests.get(self.url, timeout=timeout)
        response.encoding = "utf-8"
        response.raise_for_status()
        logger.info(f"{self.url} - <{response.status_code}>")
        return response.text