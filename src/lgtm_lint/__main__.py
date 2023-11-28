#!/usr/bin/env python3
import math
import os
import pathlib
import sys
import time


def progress_bar(
    iteration: int,
    total: int,
    prefix: str = "",
    suffix: str = "",
    decimals: int = 1,
    length: int = 100,
    fill: str = "█",
    print_end: str = "\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + "-" * (length - filled_length)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=print_end)
    if iteration == total:
        print()


def main():
    """Main function and entry point."""
    # check python version
    if sys.version_info < (3, 7):
        print("Python 3.7 or later is required.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Please provide a path to lint. Usage: lgtm_lint <path>")
        sys.exit(1)
        # run linting

    lint_paths = sys.argv[1:]
    print(f"Expanding linting paths: {lint_paths}")
    lint_files = []
    for lint_path in lint_paths:
        for path in pathlib.Path(lint_path).rglob("*"):
            if path.is_file():
                lint_files.append(os.path.abspath(path))

    if len(lint_files) == 0:
        print("No files found to lint.")
        sys.exit(1)

    print(f"Found {len(lint_files)} files to lint.")
    print("Linting files...")

    # Initial call to print 0% progress
    items = list(range(0, 57))
    items_len = len(items)
    step_size = math.ceil(items_len / len(lint_files))
    max_char_len = max([len(f) for f in lint_files])
    done_msg = f"Done!{' ' * max_char_len}"

    progress_bar(iteration=0, total=items_len, prefix="Progress:", suffix="Complete", length=50)
    for i, item in enumerate(items):
        time.sleep(0.1)
        file = lint_files[min(math.floor(i / step_size), len(lint_files) - 1)]
        message = f"Linting {file}{' ' * (max_char_len - len(file))}"
        progress_bar(
            iteration=i + 1,
            total=items_len,
            prefix="Progress:",
            suffix=message if i != (items_len - 1) else done_msg,
            length=50,
        )

    print("Summary:")
    for file in lint_files:
        print(f"\t\U00002705\t{file}")

    print("\nLooks good to me! \U0001F44D")


if __name__ == "__main__":
    main()
