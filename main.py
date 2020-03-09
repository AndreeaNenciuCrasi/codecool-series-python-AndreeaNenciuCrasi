from flask import Flask, render_template, url_for
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


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
