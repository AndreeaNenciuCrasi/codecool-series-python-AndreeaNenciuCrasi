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
