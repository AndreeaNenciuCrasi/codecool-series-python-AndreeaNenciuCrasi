from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_first_15_shows():
    return data_manager.execute_select("SELECT shows.id, shows.title, shows.year, shows.runtime, shows.trailer, shows.homepage, shows.rating, "
                                       "string_agg(DISTINCT genres.name, ', ') AS genres "
                                       "FROM shows "
                                       "LEFT JOIN show_genres ON shows.id = show_genres.show_id "
                                       "LEFT JOIN genres ON show_genres.genre_id = genres.id "
                                       "GROUP BY shows.id "
                                       "ORDER BY shows.rating DESC LIMIT 15;")

def get_show_data(show_id):
    return data_manager.execute_select(f"SELECT shows.title, shows.year, shows.runtime, shows.trailer, shows.overview, string_agg(DISTINCT genres.name, ',') AS genres FROM shows LEFT JOIN show_genres ON shows.id = show_genres.show_id LEFT JOIN genres ON show_genres.genre_id = genres.id WHERE show_id={show_id} "
                                       f"GROUP BY  shows.title, shows.year, shows.runtime, shows.trailer, shows.overview;")

def get_show_actors(show_id):
    return data_manager.execute_select(f"SELECT shows.id, show_characters.character_name, actors.name FROM shows "
                                       f"LEFT JOIN show_characters ON shows.id = show_characters.show_id "
                                       f"LEFT JOIN actors ON show_characters.actor_id = actors.id WHERE show_id={show_id};")
