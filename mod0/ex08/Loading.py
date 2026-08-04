import os
from tqdm import tqdm
from time import sleep

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    if total == 0:
        print("0")
        return
    start_time = os.times().elapsed #time it started
    terminal_length = os.get_terminal_size().columns
    progress_count_len = len(str(total))
    bar_total_range = terminal_length - (len("100%|[") + len("]| ") + ((progress_count_len) * 2) + len("/  "))
    # print(terminal_length)
    # print(bar_total_range)
    # print(progress_bar)

    for elem in lst:
        passed_time = os.times().elapsed - start_time
        percent = ((elem + 1) / total) * 100
        percent_str = (str(int(percent)) + "%").rjust(4) # just content to right
        filled = int(((elem + 1) / total) * bar_total_range)
        progress_bar = (("=" * (filled)) + ">").ljust(bar_total_range)
        progress_count = str(elem).rjust(progress_count_len)

        print(f"\r{percent_str}|[{progress_bar}]| {progress_count}/{total}", end = "", flush = True)

        yield elem

    progress_count = str(total).rjust(progress_count_len)
    print(f"\r{percent_str}|[{progress_bar}]| {progress_count}/{total}", end = "", flush = True)


def main():
    # for i in range(6):
    #     print(f"\rA processar item {i} de 5...", end="", flush=True)
    #     time.sleep(1)

    for elem in ft_tqdm(range(1)):
        sleep(0.01)
    print()


    for elem in tqdm(range(1)):
        sleep(0.05)



if __name__ == "__main__":
    main()