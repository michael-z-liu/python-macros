def apply_default_settings(np=None, pd=None):
    if np:
        np.set_printoptions(suppress=True, precision=2, threshold=3)

    if pd:
        pd.set_option("display.width", 200)
        pd.set_option("display.max_columns", 20)
