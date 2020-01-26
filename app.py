from flask import Flask, render_template, redirect
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
    return redirect(
      "https://docs.google.com/forms/d/e/1FAIpQLSctON392nRzdj9bQS7QpsddOpjpUBvLRkq1F9dTLRtLsYHJ2A/viewform?usp=sf_link"
    )


@app.template_filter("direction_filter")
def direction_filter(tours, direction):
    tours_from_direction = filter(lambda p: p[1]['departure'] == direction,
                                  tours.items())
    return dict(tours_from_direction)


@app.template_filter("best_nth")
def best_nth(tours, by="stars", n=6):
    tours = list(tours.items())
    tours.sort(key=lambda tour: tour[1][by], reverse=True)
    return dict(tours[:n])


if __name__ == "__main__":
    app.run(debug=True)
