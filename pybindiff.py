# -*- coding: utf8 -*-
import os


def main(full_path0, full_path1):
    size_list = map(get_file_size, (full_path0, full_path1))

    print("size_list = %r" % size_list)

    block_size = 1024 * 32

    block_counter = 0

    not_end_of_file = True

    b_same = True

    with open(full_path0, 'rb') as file0:
        with open(full_path1, 'rb') as file1:
            while not_end_of_file:
                block0 = file0.read(block_size)
                block1 = file1.read(block_size)

                if not all((block0, block1)):
                    not_end_of_file = False
                    break

                if block0 != block1:
                    print("block %d not equal" % (block_counter))
                    b_same = False

                block_counter += 1

    if b_same:
        print("all blocks same")
    else:
        print("different")


def get_file_size(path):
    # os.stat
    statinfo = os.stat(path)
    return statinfo.st_size


if __name__ == '__main__':
    import sys

    if 3 == len(sys.argv):
        # number of arguments
        filename0, filename1 = sys.argv[1], sys.argv[2],

        main(filename0, filename1)
