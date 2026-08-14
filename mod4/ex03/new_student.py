from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_letters, k=15))


@dataclass
class Student:
    name: str
    surname: str

    active: bool = field(init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.active = True
        self.login = self.name[0] + self.surname.lower()
        self.id = generate_id()


def main():
    student = Student(name="Edward", surname="agle")
    print(student)
    # Error
    # student = Student(name = "Edward", surname = "agle", id = "toto")


if __name__ == "__main__":
    main()
