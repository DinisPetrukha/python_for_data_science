KEYWORDS = ["mean", "median", "quartile", "std", "var"]

def ft_statistics(*args: any, **kwargs: any) -> None:
    print("args:", args, type(args))
    print("kwargs:", kwargs, type(kwargs))

    try:
        if not all(isinstance(x, (int, float)) for x in args):
            raise ValueError

        # for value in kwargs.values():
        #     if value not in KEYWORDS:
        #         raise ValueError

        if not all(type(value) is str and value.lower() in KEYWORDS for value in kwargs.values()):
            raise ValueError

        for operation in kwargs.values():
            if operation == "mean":
                sum_values = sum(args)
                n = len(args)
                result = sum_values / n
                print(f"mean : {result}")

            elif operation == "median":
                n_values = len(args)
                sort = sorted(args)
                if int(n_values % 2) == 0:
                    position = (n_values // 2) - 1
                    result = (sort[position] + sort[position + 1]) / 2
                else:
                    position = ((n_values + 1) // 2) - 1
                    result = sort[position]
                # print(f"index : {position}")
                print(f"median : {result}")


            elif operation == "quartile":
                

            # elif operation == "standard deviation":

            # elif operation == "variance":


    except Exception as msg:
        print(f"ERROR {msg}")





def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    # print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    # print("-----")
    # ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()