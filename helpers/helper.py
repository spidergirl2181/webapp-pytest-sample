import requests

"""
Create a GET request to an URL parameterized
"""
def request_get(url, payload):
    return requests.get(url, payload)

"""
Returns a JSON object of the result 
(if the result was written in JSON format, if not it raises an error)
"""
def json_loader(re):
        return re.json()

"""
Returns a value of any key from a JSON object (dictionary)
"""
def json_parser(j_obj, dict_k):
    return j_obj.get(dict_k)

"""
Wrapper for response parsing
"""
def response_parser(url, payload, dict_k):
    r = request_get(url, payload)
    e = json_loader(r)
    return json_parser(e, dict_k)