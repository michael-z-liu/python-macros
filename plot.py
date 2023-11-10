from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as colormap

import numpy as np

from .math import round_up


def close_all():
    plt.close("all")


def customise_axis(
    ax: plt.Axes,
    xlabel: str = "",
    ylabel: str = "",
    zlabel: str = "",
    title: str = "",
    grid: bool = False,
    legend_loc: str = "",
    facecolor_rgba: tuple[float, float, float, float] = (),
    xlims: tuple[float, float] = (),
    ylims: tuple[float, float] = (),
    xticks: tuple[float, ...] = (),
    xticklabels: tuple[str, ...] = (),
    yticks: tuple[float, ...] = (),
    yticklabels: tuple[str, ...] = (),
):
    if xlabel:
        ax.set_xlabel(xlabel, fontweight="bold")

    if ylabel:
        ax.set_ylabel(ylabel, fontweight="bold")

    if zlabel:
        ax.set_ylabel(zlabel, fontweight="bold")

    if title:
        ax.set_title(title, fontweight="bold")

    if grid:
        ax.grid(alpha=0.3)

    if legend_loc:
        ax.legend(loc=legend_loc)

    if len(facecolor_rgba) == 4:
        ax.set_facecolor(facecolor_rgba)

    if len(xlims) == 2:
        ax.set_xlim(xlims[0], xlims[1])

    if len(ylims) == 2:
        ax.set_ylim(ylims[0], ylims[1])

    if xticks:
        ax.set_xticks(xticks)

    if xticklabels:
        ax.set_xticklabels(xticklabels)

    if yticks:
        ax.set_yticks(yticks)

    if yticklabels:
        ax.set_yticklabels(yticklabels)


def add_invisible_square(ax: plt.Axes, half_width: float = 1):
    ax.axhline(half_width, alpha=0)
    ax.axhline(-half_width, alpha=0)
    ax.axvline(half_width, alpha=0)
    ax.axvline(-half_width, alpha=0)


def add_crosshair(
    ax: plt.Axes,
    x: Optional[float] = 0,
    y: Optional[float] = 0,
    color: str = "silver",
    zorder: float = -1,
):
    if x is not None:
        ax.axhline(x, color=color, zorder=zorder)
    if y is not None:
        ax.axvline(y, color=color, zorder=zorder)


def match_xlims(all_axes: list[plt.Axes]):
    xmin = None
    xmax = None
    for ax in all_axes:
        xmin_, xmax_ = ax.get_xlim()
        xmin = xmin_ if xmin is None else min(xmin, xmin_)
        xmax = xmax_ if xmax is None else max(xmax, xmax_)
    for ax in all_axes:
        ax.set_xlim(xmin, xmax)


def match_ylims(all_axes: list[plt.Axes]):
    ymin = None
    ymax = None
    for ax in all_axes:
        ymin_, ymax_ = ax.get_ylim()
        ymin = ymin_ if ymin is None else min(ymin, ymin_)
        ymax = ymax_ if ymax is None else max(ymax, ymax_)
    for ax in all_axes:
        ax.set_ylim(ymin, ymax)


def make_yaxis_symmetrical(ax: plt.Axes):
    val = np.abs(ax.get_ylim()).max()
    ax.set_ylim(-val, val)


def make_xaxis_symmetrical(ax: plt.Axes):
    val = np.abs(ax.get_xlim()).max()
    ax.set_xlim(-val, val)


def add_identity_line(ax: plt.Axes, config: Optional[dict] = None):
    config_ = dict(color="silver", alpha=1.0, zorder=-1)
    if config:
        config_.update(config)
    val_min = min(ax.get_xlim()[0], ax.get_ylim()[0])
    val_max = max(ax.get_xlim()[1], ax.get_ylim()[1])
    ax.plot([val_min, val_max], [val_min, val_max], **config_)


def array_to_colormap(
    array: np.ndarray, cmap_name: str = "jet", symmetrical: bool = False
):
    # source: https://stackoverflow.com/questions/26108436/how-can-i-get-the-matplotlib-rgb-color-given-the-colormap-name-boundrynorm-an
    cmap = plt.get_cmap(cmap_name)
    norm = mpl.colors.Normalize(
        vmin=float(np.nanmin(array) if not symmetrical else -np.nanmax(np.abs(array))),
        vmax=float(np.nanmax(array) if not symmetrical else np.nanmax(np.abs(array))),
    )
    scalar_map = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

    return scalar_map.to_rgba(array)


def get_gridspec_kwargs(
    width_ratios: Optional[list[int]] = None, height_ratios: Optional[list[int]] = None
) -> dict:
    kwargs = {}
    if width_ratios:
        kwargs["width_ratios"] = width_ratios
    if height_ratios:
        kwargs["height_ratios"] = height_ratios
    return {"gridspec_kw": kwargs}


def get_optimal_nrows_ncols(total: int) -> tuple[int, int]:
    nrows = int(np.sqrt(total)) - 1
    ncols = round_up(total / nrows)
    return nrows, ncols


def get_default_fig_params(**kwargs) -> dict:
    return {
        "figsize": kwargs.get("figsize", (25, 12)),
        "clear": kwargs.get("clear", True),
        "tight_layout": kwargs.get("tight_layout", True),
    }
