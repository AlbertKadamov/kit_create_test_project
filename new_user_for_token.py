import configuration
import data
import requests

def new_user():
    return requests.post(configuration.URL_SERVISE + configuration.CREATE_USER,
                        headers=data.header,
                        json=data.new_user_for_token)

response = new_user()
print(response.json())