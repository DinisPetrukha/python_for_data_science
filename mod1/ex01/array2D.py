import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of a 2D array and returns the sliced sublist.

    Args:
        family (list): A 2D list containing rows of data.
        start (int): Starting index for slicing.
        end (int): Ending index for slicing.

    Returns:
        list: Sliced sublist between the start and end indices.
    """
    try:
        assert isinstance(family, list), "Family should be an list"
        sublist_length = map(lambda line: len(family[0]) == len(line), family)
        assert all(sublist_length), "All sub-lists should be the same length"
        assert (
            isinstance(start, int) and isinstance(end, int)
            ), "Limits should be int"

        array_family = np.array(family)
        lines, columns = array_family.shape
        print(f"My shape is : ({lines}, {columns})")

        slice_f = slice(start, end)
        array_family = array_family[slice_f]
        lines, columns = array_family.shape
        print(f"My new shape is : ({lines}, {columns})")

        return array_family.tolist()

    except AssertionError as msg:
        print(f"Assertion Error: {msg}")
        return []


def main():
    """Executes test cases to demonstrate the slice_me
    function functionality."""
    family = (
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
            )

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
