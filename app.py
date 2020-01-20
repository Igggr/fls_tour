from flask import Flask, render_template
from data import title, subtitle, description, departures, tours


app = Flask('st')


@app.route('/')
def index():
    return render_template('index.html', tours=tours,
                           title=title, subtitle=subtitle,
                           description=description, departures=departures)


@app.route('/from/<direction>/')
def from_direction(direction):
    return render_template('direction.html', direction=direction,
                           departures=departures, tours=tours)


@app.route('/tours/<int:id>/')
def tour_page(id):
    return render_template('tour.html', tour=tours[id],
                           id=id, departures=departures)


@app.route("/order/<int:id>/")
def order(id):
    return f"<h1>page for buying tour {id} is under development</h1>"


@app.template_filter("direction_filter")
def direction_filter(tours, direction):
    tours_from_direction = filter(lambda p: p[1]['departure'] == direction,
                                  tours.items())
    return dict(tours_from_direction)


if __name__ == "__main__":
    app.run()
