from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')

def get_first_15_shows():
    return data_manager.execute_select('SELECT title, year, runtime, rating FROM shows ORDER BY rating DESC LIMIT 15;')
