from flask import Flask, render_template, redirect, request, url_for, jsonify, make_response
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


# @app.route('/api/display-shows-data-in-table')
# def data_shows_display_table():
#     shows = queries.get_first_15_shows()
#     list_of_dictionary = []
#     shows_dictionary = {}
#     show_dict = {}
#     for show in shows:
#         show_dict['id'] = show['id']
#         show_dict['title'] = show['title']
#         show_dict['year'] = str(show['year'])
#         show_dict['runtime'] = show['runtime']
#         show_dict['trailer'] = show['trailer']
#         show_dict['homepage'] = show['homepage']
#         show_dict['rating'] = float(show['rating'])
#         show_dict['genres'] = show['genres']
#         list_of_dictionary.append(show_dict)
#     i = 0
#     while i < len(list_of_dictionary):
#         shows_dictionary[i] = list_of_dictionary[i]
#         i = i + 1
#     return jsonify(shows_dictionary)


@app.route('/details/<show_id>')
def display_show_details(show_id):
    shows = queries.get_first_15_shows()
    show_details = queries.get_show_data(show_id)
    show_actors = queries.get_show_actors(show_id)
    seasons = queries.get_seasons(show_id)
    return render_template('show.html', shows=shows, show_details=show_details, show_actors=show_actors, seasons=seasons)


@app.route('/api/sort-by-title', methods=['POST'])
def display_table_sorted_by_title():
    if request.json['column'] == 'shows.title':
        input_column = 2
    sort_shows_by_title = queries.get_first_15_shows_sorted_by_column(input_column)
    print(sort_shows_by_title)
    # return redirect(url_for('design', sort_shows_by_title=sort_shows_by_title))
    return render_template('index.html', sort_shows_by_title=sort_shows_by_title)

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
