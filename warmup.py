import json

with open('input-formatted.json', 'r') as f:
    data = json.load(f)
    for movie in data:
        print(movie['picture_url'])