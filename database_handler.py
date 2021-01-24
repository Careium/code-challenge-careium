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


def get_cursor():
    try:
        connection = sqlite3.connect('db/traffic.db')
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        logging.error("get_curese error: " + str(e))


def insert_user_to_db(json_request):
    try:
        cursor = get_cursor()

        idd = json_request['id']
        user_type = json_request['userType']
        latitude = json_request['latitude']
        longitude = json_request['longitude']
        user_object = (idd, user_type, latitude, longitude)

        insert_query = '''INSERT INTO user (id, userType, latitude, longitude) VALUES(?,?,?,?)'''
        cursor.execute(insert_query, user_object)

        cursor.execute("SELECT * FROM user WHERE id=?", (idd,))
        rows = cursor.fetchall()

        count = 0
        for row in rows:
            logging.info(row)
            count = count + 1

        if count == 1:
            logging.info("user added successfully to the user table")
            return True
        else:
            return False
    except Exception as e:
        logging.error("Insert a user {0}".format(str(e)))
        return False
