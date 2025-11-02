import time
import logging

logger = logging.getLogger(__name__)

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"********* Time taken to process {end_time - start_time} ************")
        return result
    return wrapper