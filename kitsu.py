import http.client

from utils import query


class KitsuClient():

    def __init__(self, url = 'kitsu.io', path = '/api/edge'):
        self.conn = http.client.HTTPSConnection(url)
        self.path = path
        self.last_response = ''

    def get(self, endpoint, args = {}):
        self.conn.request('GET', self.path + '/' + endpoint + '?' + query.QueryBuilder(args).getHttpQueryString())
        self.last_response = self.conn.getresponse().read()
        return self.last_response

    def getLastResponse(self):
        return self.last_response
