class calculator:
    """class calculator"""
    def __init__(self, vec: list):
        "initializing the vector"
        self.vec = vec

    def __add__(self, object) -> None:
        """Add method"""
        self.vec = [it + object for it in self.vec]
        print(self.vec)

    def __mul__(self, object) -> None:
        """Multiply method"""
        self.vec = [it * object for it in self.vec]
        print(self.vec)

    def __sub__(self, object) -> None:
        """Subtract method"""
        self.vec = [it - object for it in self.vec]
        print(self.vec)

    def __truediv__(self, object) -> None:
        """Divide method"""
        try:
            self.vec = [it / object for it in self.vec]
            print(self.vec)
        except Exception as msg:
            print(f"{msg}")


def main():
    """Main program for tester"""
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
    v3 / 0


if __name__ == "__main__":
    main()
