from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self):
        """Return vector representation of Baratheon."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """Return string representation of Baratheon."""
        return self.__repr__()

    def die(self):
        """Change character health state to dead."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        """Return vector representation of Lannister."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """Return string representation of Lannister."""
        return self.__repr__()

    def die(self):
        """Change character health state to dead."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Factory method to create a Lannister instance."""
        return cls(first_name, is_alive)


def main():
    """Main tester"""
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(
        f"Name : {Jaine.first_name, type(Jaine).__name__}, "
        f"Alive : {Jaine.is_alive}"
    )


if __name__ == "__main__":
    main()
