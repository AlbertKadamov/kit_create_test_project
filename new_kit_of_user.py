import requests
import configuration
import data


def new_kit(kit_body):
    return requests.post(configuration.URL_SERVISE + configuration.CREATE_KIT,
                         headers=data.headers,
                         json=kit_body)
