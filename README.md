# damals

![damals logo](assets/damals.svg)

A tour around Leipzig based on historic photos.

## Roadmap

## Preprocessing

### Prepare Stadtarchiv

1. First we need to extract all information from the provived csv file, 
   and convert it to a more convenient form (JSON).
   
   ```zsh
   $ python preprocessing/preprocess_stadtarchiv.py 
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
 
 1. 
 
 
 # License
 
Code/Software: GNU General Public License v3
Media: CC-BY-SA 3.0 Museum für Druckkunst and olf42
