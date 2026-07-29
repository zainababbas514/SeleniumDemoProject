import datetime
import logging
import inspect

def get_logger():
    logger_name = inspect.stack()[1].function

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler = logging.FileHandler(f"logs/logs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)


    return logger