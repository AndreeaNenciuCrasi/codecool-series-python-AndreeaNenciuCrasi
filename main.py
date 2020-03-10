from flask import Flask, render_template, redirect, request, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/index')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/')
@app.route('/design')
def design():
    shows = queries.get_first_15_shows()
    return render_template('design.html', shows=shows)


@app.route('/details/<show_id>')
def display_show_details(show_id):
    shows = queries.get_first_15_shows()
    show_details = queries.get_show_data(show_id)
    show_actors = queries.get_show_actors(show_id)
    seasons = queries.get_seasons(show_id)
    return render_template('show.html', shows=shows, show_details=show_details, show_actors=show_actors, seasons=seasons)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
