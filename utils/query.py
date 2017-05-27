class QueryBuilder():
    def __init__(self, args):
        self.args = args

    def getHttpQueryString(self):
        query_string = []
        for key, value in self.args.items():
            if (type(value) == dict):
                query_string.append(key + self.httpBuildQuerySubArgs(value))
            elif (type(value) == list):
                query_string.append(key + '=' + ','.join(value))
            else:
                value = str(value)
                query_string.append(key + '=' + value)
        return '&'.join(query_string)

    def httpBuildQuerySubArgs(self, args):
        query_string = []
        for key, value in args.items():
            value = str(value)
            query_string.append('[' + key + ']=' + value)
        return '&'.join(query_string)
