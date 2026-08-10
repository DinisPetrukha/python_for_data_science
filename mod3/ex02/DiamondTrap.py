from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King"""
    # By doind __dict__ we access directly the variables
    # without calling the propriety functions
    def set_eyes(self, color: str):
        """Setter for eyes attribute modifying __dict__ directly."""
        self.__dict__['eyes'] = color

    def get_eyes(self):
        """Getter for eyes attribute accessing __dict__ directly."""
        return self.__dict__['eyes']

    def set_hairs(self, color: str):
        """Setter for hairs attribute, removing old 'hair' key if present."""
        self.__dict__['hairs'] = color

    def get_hairs(self):
        """Getter for hairs attribute accessing __dict__ directly."""
        return self.__dict__['hairs']

    eyes = property(get_eyes, set_eyes)
    hairs = property(get_hairs, set_hairs)


def main():
    """Main function to test King class properties and methods."""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

    # Using proprieties
    print("\nTests using proprieties")
    Joffrey.hairs = "purple"
    print(Joffrey.hairs)

    Joffrey.eyes = "purple"
    print(Joffrey.eyes)


if __name__ == "__main__":
    main()
