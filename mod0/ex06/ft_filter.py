def iterable_function1(it):
    """Returns True if even"""
    if it % 2 == 0:
        return True


def ft_filter(func, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if func is None:
        newlist = [it for it in iterable if it]
    else:
        newlist = [it for it in iterable if func(it)]
    return newlist


def main():
    """Program that mimics the original filter function"""
    print("---Original definition:")
    print(filter.__doc__)
    print("\n---Homemade definition:")
    print(ft_filter.__doc__)
    # li1 = [1, 2, 3, 4, 5, 6, 7, 8]
    # li2 = [0, 1, False, 2, "", 3, None]
    li3 = ["Ana", "Tiago", "Mateus", False, True, 1]

    print("---Original Filter")
    filtered = filter(None, li3)
    print(list(filtered))
    print()
    print("---Homemade Filter")
    filtered = ft_filter(None, li3)
    print(list(filtered))


if __name__ == "__main__":
    main()
