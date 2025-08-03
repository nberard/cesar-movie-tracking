import urllib
import json

DATA_IDF_PREFIX = "https://data.iledefrance.fr/api/datasets/1.0/films-soutenus-par-la-region-et-recompenses-aux-cesar/images/"

url_opener = urllib.URLopener()
with open('/app/input-formatted.json', 'r') as f:
    data = json.load(f)
    for movie in data:
        if DATA_IDF_PREFIX in movie['picture_url']:
            print(movie['picture_url'])
            filename =  "/app/cache/" + movie['picture_url'].split("/")[-1] + ".jpg"
            url_opener.retrieve(movie['picture_url'], filename)
            print(filename)
