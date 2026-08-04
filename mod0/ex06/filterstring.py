import sys
from ft_filter import ft_filter


def main():
    """Program that accepts two arguments: a string (S)
and an integer (N). The program should output a list
of words from S that have a length greater than N."""
    argv = sys.argv
    try:
        assert len(argv) == 3, "the arguments are bad"
        string = argv[1]
        try:
            length = int(argv[2])
        except ValueError:
            # raise forces an AssertionError
            raise AssertionError("the arguments are bad")
        splitted_string = string.split()

        result = ft_filter(lambda s: len(s) > length, splitted_string)
        print(result)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
