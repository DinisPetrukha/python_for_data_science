import os
import time
from tqdm import tqdm
import random

# def ft_tqdm(lst: range) -> None:

def show_status():
    print("1")
    yield
    print("2")
    yield
    print("3")

def find_letter_occurences(words, letter):
    for word in words:
        yield word.count(letter)

def infinite_generator(colors):
    while True:
        yield random.choice(colors)

def main():
    # for i in tqdm(range(1000)):
    #     time.sleep(0.1)
    status = show_status()
    next(status)
    time.sleep(0.1)
    next(status)
    time.sleep(0.1)

    words = ["apple", "banana", "cherry"]
    letter = "a"
    output = find_letter_occurences(words, letter)
    print("First attempt:")
    for value in output:
        print(value)
    print("Second attempt:")
    for value in output:
        print(value)

    ##infinite generator
    output_colors = infinite_generator(["blue", "grey", "pitontchic"])
    for i in range(15):
        print(next(output_colors))





if __name__ == "__main__":
    main()