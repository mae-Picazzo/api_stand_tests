import configuration
import requests
import data

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=user_body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def get_users_table():
        return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH, headers=data.headers)
