#!/usr/bin/env python3
"""
This script fetches the images of the dataset provided by Stadtarchiv Leipzig for Coding Da Vinci Ost 2018.
"""

import csv
import json

from os.path import dirname, abspath, join


# CONSTANTS
BASE_PATH = dirname(abspath(__file__))
DATA_PATH = join(BASE_PATH, "..", "rawdata", "stadtarchiv")
METADATA_FILE = join(DATA_PATH, "StadtAL_CodingDaVinci.csv")
FETCH_URLS_FILE = join(DATA_PATH, "stadtarchiv_urls.txt")

# We define the header manually because there are strange symbols in the csv file :/
HEADER = ['Archivsignatur',
          'Bezeichnung',
          'Ort',
          'Gebäude',
          'Straßen',
          'Fotograf',
          'ergänzende Datierung',
          'Datierung',
          'Copyright',
          'Lizenz',
          'URL Datensatz',
          'URL Datei']
URL_FIELD = HEADER[11]

def get_metadata(metadata_file=METADATA_FILE):
    with open(metadata_file) as mfile:
        meta_reader = csv.reader(mfile, delimiter=";")
        # skip the header
        next(meta_reader)
        for row in meta_reader:
            yield dict(zip(HEADER, row))


def save_metadata_and_write_urls(fetch_urls_file=FETCH_URLS_FILE):
    fetch_urls = []
    for metadata in get_metadata():

        fetch_url = metadata[URL_FIELD]
        meta_filename = fetch_url.split('/')[-1].split(".")[0]+".json"

        with open(join(DATA_PATH, meta_filename), "w") as mfile:
            json.dump(metadata, mfile)

        fetch_urls.append(fetch_url)

    with open(fetch_urls_file, "w") as fetch_file:
        for fetch_url in fetch_urls:
            fetch_file.write(fetch_url+"\n")

def main():
    save_metadata_and_write_urls()

if __name__ == "__main__":
    main()
