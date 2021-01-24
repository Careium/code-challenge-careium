import logging


def is_user_valid(json_request):
    try:
        idd = json_request['id']
        user_type = json_request['userType']
        latitude = json_request['latitude']
        longitude = json_request['longitude']
        if not (isinstance(idd, str) and
                isinstance(user_type, str) and
                isinstance(latitude, int) and
                isinstance(longitude, int)):
            return False
        return True
    except Exception as e:
        logging.error("Exception user validation:" + str(e))
        return False
