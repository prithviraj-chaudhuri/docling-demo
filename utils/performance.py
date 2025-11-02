import time
import logging

logger = logging.getLogger(__name__)

performance_data = {}

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        module = func.__module__
        time_taken = end_time - start_time
        if module not in performance_data:
            performance_data[module] = [time_taken]
        else:
            performance_data[module].append(time_taken)
        return result
    return wrapper

def get_metrics():
    logger.info("Total performance metrics")
    for key in performance_data:
        logger.info(f"*********** {key} \t {sum(performance_data[key])}")