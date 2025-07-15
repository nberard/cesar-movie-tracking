import json
output = {}
with open('input.json') as fp:
    output['movies'] = []
    data = json.load(fp)
    for movie in data:
        for key, value in movie.items():
            print(f'{key}: {value}')

        formatted_movie = {
            'title': movie['titre_du_film'],
            'director': movie['realisation'],
            'createdYear': movie['annee'],
            'nominationYear': movie['annee_de_la_ceremonie'],
            'nominationsCount': movie['nominations'],
            'cesarsCount': movie['nbre_cesar'],
            'href_url': movie['fiche_cesar'],
            'picture_url': movie['url_image'],
            'rewards': movie['recompenses_html'],
        }
        output['movies'].append(formatted_movie)


with open('output.json', 'w') as fp:
    json.dump(output, fp)