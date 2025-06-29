import logging
import sys

def get_logger(name: str = __name__ ) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)  # Should be INFO when not actively being developed

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(filename)s:%(lineno)d | [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.propagate = False    # Avoid duplicate logs if used in libraries
    return logger
