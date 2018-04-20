#!/usr/bin/env python3
"""
This script fetches the images of the dataset provided by Stadtgeschichtliches Museum Leipzig
for Coding Da Vinci Ost 2018.
"""

import openpyxl
import json

from os.path import dirname, abspath, join


# CONSTANTS
BASE_PATH = dirname(abspath(__file__))
DATA_PATH = join(BASE_PATH, "..", "rawdata", "stadtgeschichtliches_museum")
METADATA_FILE = join(DATA_PATH, "Metadaten_SGM.xlsx")


def extract_metadata(metadata_file=METADATA_FILE):
    wb = openpyxl.load_workbook(metadata_file)

    for sheet_name in wb.sheetnames:
        sheet = wb[sheet_name]
        data = dict()
        object_name = sheet_name.lower().split(" ")[1]
        for row in sheet:
            key = row[0].value.strip()
            value = row[1].value.strip()
            data[key] = value
        with open(join(DATA_PATH, object_name+".json"), "w") as out_file:
            json.dump(data, out_file, indent=4)

def main():
    extract_metadata()

if __name__ == "__main__":
    main()
