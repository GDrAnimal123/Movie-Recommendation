import json
import urllib.parse
from urllib.request import urlopen


def call_omdb_api(attribute, query):
    omdbapi_url = "http://www.omdbapi.com/?apikey=953618a6&"
    query_url = urllib.parse.urlencode([(query, attribute)])

    with urlopen(omdbapi_url + query_url) as response:
        source = response.read()

    return json.loads(source)


def get_result_from_api(attribute, query=""):
    result = None
    if attribute and query:
        # If valid content and command
        data = call_omdb_api(attribute, query)
        if data["Response"] != "False":
            if query == "i":
                result = data
            elif query == "s":
                result = data["Search"]

    return result
