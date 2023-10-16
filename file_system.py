import os, pathlib, glob
from typing import Union


def find_files_by_extension(
    root: Union[os.PathLike, str], extension: str, recursive: bool = True
) -> list[os.PathLike]:

    pathlib.Path(root)

    files = [
        pathlib.Path(path)
        for path in glob.iglob(f".\\{root}\\**\\*.{extension}", recursive=recursive)
    ]

    return files
