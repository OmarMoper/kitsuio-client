"Kitsu client"
import http.client

from .utils import query
import urllib

class KitsuClient():
    "Allows make http requests to kitsu api."

    def __init__(self, url = 'kitsu.io', path = '/api/edge'):
        "Constructor. Indicates api url with {url} and api main path with {path}."
        self.conn = http.client.HTTPSConnection(url)
        self.path = path
        self.last_response = ''

    def get(self, endpoint, args = {}):
        "Make http request to api. Indicate endpoint with {endpoint} and path with {path}. Returns string with last response"
        url = self.path + '/' + endpoint + '?' + query.QueryBuilder(args).getHttpQueryString()
        self.conn.request('GET', url.replace(' ', '%20'))
        self.last_response = self.conn.getresponse()
        return self.last_response.read().decode()

    def getLastResponse(self):
        "Get last response object (http.client.response)."
        return self.last_response
