import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for given height and weight lists.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: A list containing the calculated BMI values.
    """
    height_types = [isinstance(n, (int, float)) for n in height]
    weight_types = [isinstance(n, (int, float)) for n in weight]
    try:
        assert len(height) == len(weight), "Arguments should be the same size"
        assert all(height_types) and all(weight_types), "Should be float / int"

        np_height = np.array(height)
        np_weight = np.array(weight)

        bmi = np_weight / (np_height ** 2)
        return bmi.tolist()

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if each BMI value in the list exceeds a specified limit.

    Args:
        bmi (list[int | float]): List of BMI values to evaluate.
        limit (int): The threshold limit to compare against.

    Returns:
        list[bool]: A list of booleans where True
        means the BMI exceeds the limit.
    """
    bmi_types = [isinstance(n, (int, float)) for n in bmi]
    try:
        assert all(bmi_types), "All bmi elements should be float or int"
        assert type(limit) is int, "Second argument should be an int"

        bmi_array = np.array(bmi)
        return (bmi_array > limit).tolist()

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
        return []


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 2))


if __name__ == "__main__":
    main()
