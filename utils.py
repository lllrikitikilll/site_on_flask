import json


def get_all_data():
    with open("data.json", 'r', encoding="utf-8") as file:
        data = json.load(file )
    return data['title']


def get_one_by_id(id_):
    data = get_all_data()
    for i in data:
        if id_ == i:
            return data[i]


print(get_one_by_id("3"))

menu = [
    {"link": "/departure/msk", "title": "Из Москвы"},
    {"link": "/departure/spb", "title": "Из Петербурга"},
    {"link": "/departure/nsk", "title": "Из Новосибирска"},
    {"link": "/departure/ekb", "title": "Из Екатеринбурга"},
    {"link": "/departure/kazan", "title": "Из Казани"},
]