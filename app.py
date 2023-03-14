from flask import Flask, render_template, request
from utils import get_all_data, get_one_by_id, search_tour

app = Flask(__name__)
# тренировочный комментарий

@app.route("/")
def index():
    data = get_all_data()
    return render_template("index.html", data=data)


@app.route("/departure/<depart>")
def departure(depart):
    
    data_all = get_all_data()
    data = {}
    info_price = []
    info_nights = []
    of = {
    "msk": "Из Москвы",
    "spb": "Из Петербурга",
    "nsk": "Из Новосибирска",
    "ekb": "Из Екатеринбурга",
    "kazan": "Из Казани"
  }
    for i in data_all:
        if data_all[i]['departure'] == depart:
            data[i] = data_all[i]
            info_price.append(data_all[i]['price'])
            info_nights.append(data_all[i]["nights"])
    return render_template("departure.html", of=of[depart], data=data, count_tour=len(data), info_price=(min(info_price),max(info_price)), info_nights=(min(info_nights),max(info_nights)))


@app.route("/tours/<id_>")
def tours(id_):
    of = {
    "msk": "Из Москвы",
    "spb": "Из Петербурга",
    "nsk": "Из Новосибирска",
    "ekb": "Из Екатеринбурга",
    "kazan": "Из Казани"
  }
    tour = get_one_by_id(id_)
    return render_template("tours.html", of=of[tour['departure']], tour=tour)

@app.route("/no")
def you_bomg():
    return render_template('Nnot_money.html')

@app.route('/search/', methods=['GET'])
def search_tour():
    tour = request.args.get('tour')
    data = get_all_data()
    tours = []
    for i in data:
        if tour.lower() in data[i]['country'].lower():
            tours.append(data[i])

    return render_template('search.html', tours=tours)

if __name__ == "__main__":
    app.run(debug=True)