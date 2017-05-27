"""Query builder. I don't use contributed library cause I didn't found anything
which supplies this kind of argument: filter[query]=anime."""

class QueryBuilder():
    "Builds http query string. {args} is a dict used to build query string"
    def __init__(self, args):
        self.args = args

    def getHttpQueryString(self):
        "Get http query string from {self.args}"
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
        "Build http query sub args. This helps to build args like this: filter[query]=anime"
        query_string = []
        for key, value in args.items():
            value = str(value)
            query_string.append('[' + key + ']=' + value)
        return '&'.join(query_string)
