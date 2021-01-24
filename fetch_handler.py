import requests
import json
import logging


def handle_area_data_from_traffic_service():
    areas_json_object = fetch_area_data()
    save_area_data_in_temp_files(areas_json_object)


def handle_message_data_from_traffic_service():
    messages_json_object = fetch_messages_data()
    save_messages_data_in_temp_files(messages_json_object)


def fetch_messages_data():
    try:
        response_message = requests.get('http://api.sr.se/api/v2/traffic/messages?format=json&indent=true')
        response_message_json = response_message.json()
        messages = response_message_json['messages']
        messages_json_object = {'messages': messages}
        return messages_json_object
    except Exception as e:
        logging.error('Exception in thread: {0}'.format(str(e)))


def save_messages_data_in_temp_files(messages_json_object):
    try:
        with open('data/temp/messages.json', 'w') as file:
            file.write(str(messages_json_object))
        with open('data/temp/messages.json.txt', 'w') as file:
            message_json_string = json.dumps(messages_json_object, indent=2)
            file.write(message_json_string)

        logging.info('All MESSAGEs are fetched and saved successfully')
    except IOError as ioe:
        logging.error('IOException in thread: {0}'.format(str(ioe)))
    except Exception as e:
        logging.error('Exception in thread: {0}'.format(str(e)))


def fetch_area_data():
    try:
        response_area = requests.get('http://api.sr.se/api/v2/traffic/areas?format=json&indent=true')
        response_area_json = response_area.json()
        areas = response_area_json["areas"]
        areas_json_object = {'areas': areas}
        return areas_json_object
    except Exception as e:
        logging.error('Exception in thread: {0}'.format(str(e)))


def save_area_data_in_temp_files(areas_json_object):
    try:
        with open('data/temp/areas.json', 'w') as file:
            file.write(str(areas_json_object))
        with open('data/temp/areas.json.txt', 'w') as file:
            area_json_string = json.dumps(areas_json_object, indent=2)
            file.write(area_json_string)

        logging.info('All AREAs are fetched and saved successfully')
    except IOError as ioe:
        logging.error('IOException in thread: {0}'.format(str(ioe)))
    except Exception as e:
        logging.error('Exception in thread: {0}'.format(str(e)))
