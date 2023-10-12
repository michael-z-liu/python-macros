def apply_default_settings(for_numpy: bool = True, for_pandas: bool = True):
    if for_numpy:
        import numpy

        numpy.set_printoptions(suppress=True, precision=2, threshold=3)

    if for_pandas:
        import pandas

        pandas.set_option("display.width", 200)
