import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    height_types = [isinstance(n, (int, float)) for n in height]
    weight_types = [isinstance(n, (int, float)) for n in weight]
    try:
        assert len(height) == len(weight), "Both input lists should be the same size"
        assert all(height_types) and all(weight_types), "All element should be float or int"

        np_height = np.array(height)
        np_weight = np.array(weight)

        bmi = np_weight / (np_height ** 2)


    except AssertionError as msg:
        print(f"AssertionError: {msg}")



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    #code