from logging import DEBUG, Formatter, Logger, StreamHandler, getLogger


def create_logger(name: str) -> Logger:
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    console = StreamHandler()
    console.setFormatter(Formatter('%(asctime)s [%(name)s] [%(levelname)s] %(message)s'))
    logger.addHandler(console)
    return logger
