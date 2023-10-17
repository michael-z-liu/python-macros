import logging


def setup(module_name: str, logging_level=logging.INFO):

    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # create logger
    logger = logging.getLogger(module_name)
    logger.setLevel(logging_level)

    # extra code patryk used
    """ 
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging_level)

    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    """


def get(module_name: str, logging_level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(module_name)
    setup(module_name, logging_level)
    return logger
