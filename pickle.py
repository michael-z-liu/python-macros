import os, pickle, sys

from . import logger

LOG = logger.get(__name__)


def save(instance: object, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pickle.dump(instance, open(path, "wb"))
    LOG.info(f"Instance of type <{type(instance).__name__}> pickled to '{path}'.")


def load(path: str):
    obj = pickle.load(open(path, "rb"))
    LOG.info(f"Instance of type <{type(obj).__name__}> loaded from '{path}'.")
    return obj
