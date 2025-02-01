import requests

URL = 'https://api.escuelajs.co/api/v1'

def get_categories():
    r = requests.get(URL + '/categories')
    print(r.status_code)
    categories = r.json()

    names_categories = list(map(lambda x: x['name'], categories))
    print(names_categories)