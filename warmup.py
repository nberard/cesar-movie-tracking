import sys
import json

DATA_IDF_PREFIX = "https://data.iledefrance.fr/api/datasets/1.0/films-soutenus-par-la-region-et-recompenses-aux-cesar/images/"

with open('/app/input-formatted.json', 'r') as f:
    data = json.load(f)
    for movie in data:
        if DATA_IDF_PREFIX in movie['picture_url']:
            print(movie['picture_url'])
            filename =  "/app/cache/" + movie['picture_url'].split("/")[-1] + ".jpg"
            if sys.version_info[0] == 3:
                from urllib.request import urlopen
            else:
                # Not Python 3 - today, it is most likely to be Python 2
                # But note that this might need an update when Python 4
                # might be around one day
                from urllib import urlopen

            with urlopen(movie['picture_url']) as fh_url:
                s = fh_url.read()
                print(s)
                print(type(s))

