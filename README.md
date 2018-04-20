# damals

![damals logo](assets/damals.svg)

A tour around Leipzig based on historic photos.

## Roadmap

## Preprocessing

Aquire the metadata files (see: [Coding Da Vinci Website](https://codingdavinci.de/daten)) 
or use the files provided in this repository.

### Prepare Stadtarchiv

1. First we need to extract all information from the provived csv file, 
   and convert it to a more convenient form (JSON).
   
   ```zsh
   $ python preprocessing/pp_sa.py 
   ```
   
   Executing this script will create a json file for each photo in the collection,
   and create a txt file with all urls.

2. Fetch the images from the server. We could have used python-requests, 
   but it's way more convenient to simply use wget and a for loop.
   
   ```zsh
   $ cd rawdata/stadtatchiv
   $ for url in `cat stadtarchiv_urls.txt`; do; wget ${url}; done 
   ```
 
 ### Prepare Stadtgeschichtliches Museum
 
 1. Run the converter script to convert the xlsx file to individual 
    JSON files.
    
    ```zsh
    $ python preprocessing/pp_sgm.py
    ```
    
    Download all images files into the *rawdata/stadtgeschichtliches_museum* 
    directory. The images are provided as *JPEG* (low resolution, ca. 
    13MB total) and *TIFF* (high resolution, ca. 2.6GB total).
 
 
 # License
 
* Code/Software: GNU General Public License v3
* Metadata: CC0 of Stadtarchiv Leipzig and Stadtgeschichtliches Museum Leipzig
* Media: CC-BY-SA 3.0 Museum für Druckkunst and olf42
