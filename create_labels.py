import json
import os

label_file = open('labels.csv', 'w')
genre = 'Genre'
imdbId = 'imdbID'

def write_label_entry(entry):
    genres = entry[genre].replace(',', '')
    entryId = entry[imdbId]
    print(entryId + ',' + genres)
    label_file.write(entryId + ',' + genres)

def add_label_entries(file):
    with open(file, 'r') as f:
        parsed_json = json.load(f)
        for entry in parsed_json:
            write_label_entry(entry)

fake_entry={'Genre': 'Action, Comedy, Drama', 'imdbID': 'coolio'}

for file in os.listdir('.'):
    if (file.endswith('.json')):
        add_label_entries(file)

label_file.close()

