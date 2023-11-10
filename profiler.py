import cProfile
import os
import pstats
import sys
from typing import Union
import pathlib


def profile_function(
    f,
    runs: int = 10,
    root: Union[os.PathLike, str] = "",
    print_results: bool = True,
    dump_results: bool = True,
    show_results: bool = True,
):
    with cProfile.Profile() as profile:

        for i in range(runs):
            f()

        results = pstats.Stats(profile)
        results.sort_stats(pstats.SortKey.TIME)
        if print_results:
            results.print_stats(20)
        if dump_results:
            results.dump_stats(pathlib.Path(root, "last.profile"))
        if show_results:
            import subprocess

            subprocess.Popen(["tuna", "last.profile"])


def view_profile():
    print(
        "The last profile will be saved in 'last.profile', which can be read using 'tuna last.profile' command in terminal.",
        file=sys.stderr,
    )
