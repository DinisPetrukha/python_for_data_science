class calculator:
    """Constructor calculator class"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Applies the dot product of two vectors and prints the result"""
        # print(list(zip(V1, V2)))
        result = sum([it[0] * it[1] for it in zip(V1, V2)])
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Sums two vectors and prints the result vector"""
        result = [float(it[0] + it[1]) for it in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts two vectors and prints the result vector"""
        result = [float(it[0] - it[1]) for it in zip(V1, V2)]
        print(f"Sous Vector is: {result}")


def main():
    """Main program for testing the calculator class"""
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
