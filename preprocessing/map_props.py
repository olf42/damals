#!/usr/bin/env python3
"""
This script matches the key value pairs of the rawdata onto our final data structure.
"""

import os
import json
import preprocessing.pp_sa as pp_sa
import preprocessing.pp_sgm as pp_sgm

from os.path import join


DATA_PATHS = [pp_sa.DATA_PATH, pp_sgm.DATA_PATH]

def get_all_keys(data_path):
    """
    Reads all json files in a directory and returns all found keys as a set.
    :param data_path: Path where the generated json files are stored.
    :return: a set of keys
    """
    keys = set()
    for filename in os.listdir(data_path):
        if filename.endswith("json"):
            with open(join(data_path, filename)) as infile:
                metadata = json.load(infile)
                for key in metadata.keys():
                    keys.add(key)
    return keys


def show_all_keys(data_paths=DATA_PATHS):
    """
    Fetchs all keys of Stadtarchiv and Stadtgeschichtliches Museum and displays them in an ordered manner.
    :return:
    """
    all_keys = []
    for data_path in data_paths:
        all_keys += list(get_all_keys(data_path))
    all_keys.sort()

    for key in all_keys:
        print(key)


def main():
    show_all_keys()


if __name__ == "__main__":
    main()