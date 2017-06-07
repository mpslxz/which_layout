import os
from collections import Counter


def find_files(root_folder, extension):
    res = []
    for root, dirs, files in os.walk(root_folder, topdown=False):
        for name in files:
            if name.endswith(extension):
                print os.path.join(root, name)
                res.append(os.path.join(root, name))
    return res


def get_char_hist(string):
    letter_hist = Counter(string.lower().replace('\n', ''))
    return letter_hist


if __name__ == "__main__":
    x = find_files('/Users/mehran/git', '.tex')
    for i in x:
        print get_char_hist(i)
