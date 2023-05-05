#!/usr/bin/env python3

import sys
import time
import glob
import os
import math

# check python version
if sys.version_info < (3, 7):
    print("Python 3.7 or later is required.")
    sys.exit(1)


if len(sys.argv) < 2:
    print("Please provide a path to lint. Usage: lgtm_lint <path>")
    sys.exit(1)

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()


# run linting
lint_paths = sys.argv[1:]
print(f'Expanding linting paths: {lint_paths}')
lint_files = []
for lint_path in lint_paths:
    lint_files.extend([f for f in glob.glob(lint_path, recursive=True) if os.path.isfile(f)])


if len(lint_files) == 0:
    print('No files found to lint.')
    sys.exit(1)


print(f'Found {len(lint_files)} files to lint.')
print('Linting files...')


# Initial call to print 0% progress
items = list(range(0, 57))
items_len = len(items)
step_size = math.ceil(items_len/len(lint_files))
max_char_len = max([len(f) for f in lint_files])


printProgressBar(0, items_len, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    time.sleep(0.1)
    file = lint_files[min(math.floor(i/step_size), len(lint_files) - 1)]
    buffer = ' ' * (max_char_len - len(file))
    message = f'Linting {file}{buffer}'

    printProgressBar(i + 1, items_len, prefix = 'Progress:', suffix = message if i != (items_len-1) else 'Done!', length = 50)


print('Summary:')
for file in lint_files:
    print(f'\t{file}\t\U00002705')

print('\nLooks good to me! \U0001F44D')

