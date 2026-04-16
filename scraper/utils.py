"""Module to implement some utils functions like decorators."""

import functools, time, logging

from requests.exceptions import HTTPError
from pathlib import Path

# Define custom logger
logger = logging.getLogger(__name__) # Define the logger name
logger.setLevel("DEBUG") # Define the log level for the global logger

console_logger = logging.StreamHandler() # Add console logger
console_logger.setLevel("WARNING") # Define the log level at WARNING

Path("docs").mkdir(parents=True, exist_ok=True) # Create the folder if it doesn't exist
file_logger = logging.FileHandler("docs/scraper.log", mode="a", encoding="utf-8") # Add file logger
file_logger.setLevel("DEBUG") # Define the log level at DEBUG

logger.addHandler(console_logger) # Add console logger
logger.addHandler(file_logger) # Add file logger

formatter = logging.Formatter(             # Define the log format
    "{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
console_logger.setFormatter(formatter) # Apply log format to console logs
file_logger.setFormatter(formatter) # Apply log format to file logs



# Retry decorator
def retry(n: int, delay: float):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            error = Exception() # Error value to Raise if function doesn't work
            for i in range(n):
                try:
                    value = func(*args, **kwargs)
                    logger.debug(f"Load data sucess!")
                    return value # Return the basic function execution if it works
                except HTTPError: # Catch if the error is fatal
                    raise # Stop the retry
                except Exception as e: # Catch the error
                    logger.warning(f"Impossible to load data at retry n°{i}") # Display in terminal the echecs
                    error = e # Update the error value for each loop lap
                    time.sleep(delay) # Delay before to execute the function another time
            logger.error(f"Impossible to load website data after {n} retries")
            raise error # Throw the error if the function doesn't work after n retry
        return wrapper_retry
    return decorator_retry


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter() # Start time before executing the function
        value = func(*args, **kwargs)
        end = time.perf_counter() # End time after executing the function
        duration = end - start # Duration calculation of the function execution
        logger.debug(f"{func.__name__} is executed in {duration:.6f}s")
        return value
    return wrapper_timer
