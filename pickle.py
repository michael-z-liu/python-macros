import os, pickle, sys


def save(instance: object, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pickle.dump(instance, open(path, "wb"))
    print(f"Instance pickled to '{path}'.", file=sys.stderr)


def load(path: str):
    obj = pickle.load(open(path, "rb"))
    print(f"Instance loaded from '{path}'.", file=sys.stderr)
    return obj
