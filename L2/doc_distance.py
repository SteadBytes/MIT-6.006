import math
import os
import string
import sys
from collections import Counter
# Document Distance using word frequency

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# translate punctuation to spaces
trans_table = str.maketrans(string.punctuation, " " * len(string.punctuation))


def file_word_frequencies(file_path):
    frequencies = Counter()
    with open(file_path) as f:
        for line in f:
            frequencies.update(line.translate(trans_table).lower().split())
    return frequencies


def inner_product(v1, v2):
    total = 0
    for key, val in v1.items():
        if key in v2:
            total += val * v2[key]
    return total


def vector_angle(v1, v2):
    return math.acos(inner_product(v1, v2) /
                     (math.sqrt(inner_product(v1, v1)) *
                      math.sqrt(inner_product(v2, v2)))
                     )


def check_files(file_paths):
    for f in file_paths:
        if not os.path.isfile(f):
            raise FileNotFoundError('Input file {} not found'.format(f))


def main():
    # pass filepaths as arguments
    if len(sys.argv) == 3:
        f1, f2 = sys.argv[1:]
    else:
        # default
        f1 = os.path.join(BASE_DIR, 'doc1.txt')
        f2 = os.path.join(BASE_DIR, 'doc2.txt')
    check_files((f1, f2))
    v1 = file_word_frequencies(f1)
    v2 = file_word_frequencies(f2)
    print('Document distance: {}'.format(vector_angle(v1, v2)))


if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
