def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculates statistical metrics on positional
    arguments based on keyword commands.

    Supported operations in kwargs:
        - "mean": Arithmetic mean.
        - "median": Middle value of ordered data.
        - "quartile": First (25%) and third (75%) quartiles.
        - "std": Population standard deviation.
        - "var": Population variance.

    Prints "ERROR" if arguments are invalid or if args is empty.
    """
    # print("args:", args, type(args))
    # print("kwargs:", kwargs, type(kwargs))

    try:
        if not all(isinstance(x, (int, float)) for x in args):
            raise ValueError

        # for value in kwargs.values():
        #     if value not in KEYWORDS:
        #         raise ValueError
        # and value.lower() in KEYWORDS
        if not all(type(value) is str for value in kwargs.values()):
            raise ValueError

        for operation in kwargs.values():
            n_values = len(args)
            sort = sorted(args)
            try:
                if operation == "mean":
                    sum_values = sum(args)
                    result = sum_values / n_values
                    print(f"mean : {result}")

                elif operation == "median":
                    if int(n_values % 2) == 0:
                        position = (n_values // 2) - 1
                        result = (sort[position] + sort[position + 1]) / 2
                    else:
                        position = ((n_values + 1) // 2) - 1
                        result = sort[position]
                    # print(f"index : {position}")
                    print(f"median : {result}")

                elif operation == "quartile":
                    q1 = int(n_values * 0.25)
                    q3 = int(n_values * 0.75)
                    # print(f"n= {n_values} q1: {q1}, q3: {q3}")
                    result = [float(sort[q1]), float(sort[q3])]
                    print(f"quartile : {result}")

                elif operation == "std" or operation == "var":
                    sum_values = sum(args)
                    mean = (sum_values / n_values)
                    sqr_deviation = [(num - mean) ** 2 for num in args]
                    sum_deviation = sum(sqr_deviation)
                    variance = sum_deviation / n_values
                    std_deviation = variance ** 0.5
                    # print(f"mean {mean}\ndeviation: {sqr_deviation}")
                    # print(f"sum_deviation {sum_deviation}")
                    # print(f"deviation: {variance}")
                    if operation == "std":
                        print(f"std : {std_deviation}")
                    else:
                        print(f"var : {variance}")
            except Exception:
                print("ERROR")

    except Exception:
        print("ERROR")


def main():
    """Main function to test ft_statistics with various test cases.

    Executes test calls with numerical data and valid/invalid keyword arguments
    to demonstrate statistical calculations and error handling.
    """
    ft_statistics(
        1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile"
        )
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(
        5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem"
        )
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
