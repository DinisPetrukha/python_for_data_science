import sys
import string


def str_analyzer(text: str):
    """Receives a str and returns the number
of all types of chars on the string"""
    total_counter = 0
    upper_counter = 0
    lower_counter = 0
    punct_counter = 0
    spaces_counter = 0
    digits_counter = 0

    for i in text:
        if i.isupper():
            upper_counter += 1
        elif i.islower():
            lower_counter += 1
        # string.punctuation its a list/collection of specific characters
        elif i in string.punctuation:
            punct_counter += 1
        elif i.isspace():
            spaces_counter += 1
        elif i.isdigit():
            digits_counter += 1
        total_counter += 1

    print(f"The text contains {total_counter} characters:")
    print(f"{upper_counter} upper letters")
    print(f"{lower_counter} lower letters")
    print(f"{punct_counter} punctuation marks")
    print(f"{spaces_counter} spaces")
    print(f"{digits_counter} digits")


def main():
    """Program that receives a str and returns the number
of all types of chars on the string"""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"

        if len(sys.argv) == 2:
            string = sys.argv[1]
        else:
            print("What is the text to count?")
            string = sys.stdin.readline()

        str_analyzer(string)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")


if __name__ == "__main__":
    main()
