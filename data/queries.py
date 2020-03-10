from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_first_15_shows():
    return data_manager.execute_select("SELECT shows.id, shows.title, shows.year, shows.runtime, shows.trailer, shows.homepage, shows.rating, string_agg(DISTINCT genres.name, ', ') AS genres FROM shows LEFT JOIN show_genres ON shows.id = show_genres.show_id LEFT JOIN genres ON show_genres.genre_id = genres.id GROUP BY shows.id ORDER BY shows.rating DESC LIMIT 15;")


def get_show_data(show_id):
    return data_manager.execute_select("SELECT shows.title, shows.year, shows.runtime, shows.trailer, shows.overview, string_agg(DISTINCT genres.name, ',') AS genres FROM shows LEFT JOIN show_genres ON shows.id = show_genres.show_id LEFT JOIN genres ON show_genres.genre_id = genres.id WHERE shows.id=%(show_id)s GROUP BY  shows.title, shows.year, shows.runtime, shows.trailer, shows.overview;", variables={"show_id": show_id})


def get_show_actors(show_id):
    return data_manager.execute_select("SELECT shows.id, show_characters.character_name, actors.name FROM shows LEFT JOIN show_characters ON shows.id = show_characters.show_id LEFT JOIN actors ON show_characters.actor_id = actors.id WHERE shows.id=%(show_id)s;", variables={"show_id": show_id})


def get_seasons(show_id):
    return data_manager.execute_select("SELECT shows.id, seasons.season_number, seasons.title, seasons.overview, COUNT(episodes.episode_number) AS episodesNumber FROM shows LEFT JOIN seasons ON shows.id = seasons.show_id LEFT JOIN episodes ON seasons.id = episodes.season_id WHERE shows.id=%(show_id)s GROUP BY shows.id, seasons.season_number, seasons.title, seasons.overview;", variables={"show_id": show_id})
