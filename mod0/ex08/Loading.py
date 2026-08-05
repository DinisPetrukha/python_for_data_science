import os
from tqdm import tqdm
from time import sleep


def ft_tqdm(lst: range) -> None:
    """"
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progress bar every time a value is requested.
    """
    total = len(lst)
    if total == 0:
        print("0")
        return
    # start_time = os.times().elapsed  # time is started
    terminal_length = os.get_terminal_size().columns
    progress_count_len = len(str(total))
    bar_elements = len("100%|[]| /  ") + ((progress_count_len) * 2)
    bar_total_range = terminal_length - bar_elements
    # print(terminal_length)
    # print(bar_total_range)

    for elem in lst:
        # passed_time = os.times().elapsed - start_time
        percent = ((elem + 1) / total) * 100
        # Adjust content to right
        percent_str = (str(int(percent)) + "%").rjust(4)
        filled = int(((elem + 1) / total) * bar_total_range)
        progress_bar = (("=" * (filled)) + ">").ljust(bar_total_range)
        progress_count = str(elem).rjust(progress_count_len)

        print(
            f"\r{percent_str}|[{progress_bar}]| {progress_count}/{total}",
            end="",
            flush=True
        )

        yield elem

    progress_count = str(total).rjust(progress_count_len)
    print(
        f"\r{percent_str}|[{progress_bar}]| {progress_count}/{total}",
        end="",
        flush=True
    )


def main():
    """
    Program calls the function ft_tqdm()
    """
    for elem in ft_tqdm(range(201)):
        sleep(0.05)
    print()

    for elem in tqdm(range(201)):
        sleep(0.05)


if __name__ == "__main__":
    main()
