import sqlite3
import logging


def init_database():
    """
    initialize the database and necessary tables

    :return: cursor
    """
    try:
        connection = sqlite3.connect('db/traffic.db')
        cursor = connection.cursor()
        create_table_user = '''CREATE TABLE IF NOT EXISTS user (
                                id TEXT PRIMARY KEY,
                                userType TEXT NOT NULL,
                                latitude INTEGER DEFAULT 0,
                                longitude INTEGER DEFAULT 0
                                );
                            '''
        cursor.execute(create_table_user)
        logging.info("user table is now available")
        return cursor
    except Exception as e:
        logging.error("Database cannot be initialized. {0}".format(str(e)))
