"""Module to implement some utils functions like decorators."""

import functools
import time

from requests.exceptions import HTTPError

# Retry decorator
def retry(n: int, delay: float):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            error = Exception() # Error value to Raise if function doesn't work
            for _ in range(n):
                try:
                    value = func(*args, **kwargs)
                    return value # Return the basic function execution if it works
                except HTTPError: # Catch if the error is fatal
                    raise # Stop the retry
                except Exception as e: # Catch the error
                    print(f"Error: {e}")
                    error = e # Update the error value for each loop lap
                    time.sleep(delay) # Delay before to execute the function another time
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
        print(f"{func.__name__} is executed in {duration:.6f}s")
        return value
    return wrapper_timer
