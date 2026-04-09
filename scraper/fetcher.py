"""This module allow to make a request and check if there is a success."""

import requests

from requests.exceptions import HTTPError


class Fetcher:
    """Class to make some requests."""

    def __init__(self, url: str) -> None:
        """Constructor initialisation"""
        self.url = url

    def make_request(self, timeout: float=1) -> str | None:
        """Make requests and handle by status code"""
        response = requests.get(self.url, timeout=timeout)
        response.encoding = "utf-8"
        response.raise_for_status()
        return response.text

