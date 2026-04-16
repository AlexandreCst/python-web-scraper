"""This module give the possibility to export the data in CSV or JSON file"""

import json, csv

from pathlib import Path

from scraper.utils import logger

class Exporter:
    """
    Exporte class
    """
    def __init__(self, products: list[dict[str, str | float]], path: str="docs"):
        """
        Constructor initialisation
        
        :param products: The list that contain a dict for each product (book)
        :param path: Path of the file to write
        :type products: list[dict[str, str | float]] 
        """
        self.products = products
        self.path = path
    
    # Method to export the data in JSON file
    def to_json(self, filename: str) -> None:
        """
        Export the products data to a JSON file

        :param filename: Name of the file to export with extension .json
        :type filename: str
        :rtype: JSON file
        """
        path = Path(f"{self.path}/{filename}") # Define the path
        path.parent.mkdir(parents=True, exist_ok=True) # Create the folder if it doesn't already exist

        with path.open(mode="w") as json_file: 
            data = json.dumps(self.products, indent=4) # Serialize in JSON
            json_file.write(data) # Write in the new file the data
        
        logger.info("Success, data are exported in a JSON file!")
    # Methode to export the data in CSV file
    def to_csv(self, filename: str) -> None:
        """
        Export the products data to a CSV file
        
        :param filename: Name of the file to export with extension .csv"""
        path = Path(f"{self.path}/{filename}") # Define the path
        path.parent.mkdir(parents=True, exist_ok=True) # Create the folder if it doesn't already exist

        with path.open(mode="w", newline="") as csv_file:
            fieldnames = ["title", "price", "availability", "rating"] # Define the header of the file
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames) 
            writer.writeheader() # Write the header of the file
            writer.writerows(self.products) # Write the data in the CSV file

        logger.info("Success, data are exported in a CSV file!")