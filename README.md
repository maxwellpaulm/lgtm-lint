# LGTM Linter
Looks good to me! This is a satirical "linter" that doesn't actually assert or check anything. Linters have become so picky and opinionated that we thought it might be refreshing to have one that is happy with your code just the way it is!

## Local Python Install
You can install this package locally by running the following from project root:
```bash
pip install -e .
```
This will automatically add `lgtm-lint` to your path.

## Legacy Install
Just run the following:
```bash
./legacy_install.sh
```
This will install the script in your user bin. Also, Python3 is required to run the linter.

## Usage
Execute the linter over any code you'd like linted! You can do this by running the following:
```bash
lgtm-lint *
```
Or a more specific file or directory, up to you.
