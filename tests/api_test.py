from helpers.helper import *


URL = 'https://api.openweathermap.org/data/2.5/weather'
PAYLOAD = {'q':'London', 'appid':'a0e90e2a192d7b986561faf882b98a22'}

CITY = ['Hanoi', 'Sydney', 'Paris']
INVALID_PAYLOAD = {'q':'Hanoi', 'appid':''}

def test_connection():
    r = request_get(URL, PAYLOAD)
    assert r.status_code == 200

def test_valid_response():
    for i in CITY:
        PAYLOAD['q'] = i
        assert(response_parser(URL, PAYLOAD, "name")) == i

def test_negative_response():
    assert response_parser(URL, INVALID_PAYLOAD, "cod") == 401

