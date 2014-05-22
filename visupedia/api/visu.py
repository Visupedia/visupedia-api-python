class Visu(object):

    """Returns an MyVisu api instance

    Args:
        key: The api key provided by Visupedia
    """

    def __init__(self, key, client):
        self.key = key
        self.client = client

    def get(self, id, lang, version, options={}):
        """Returns all information about the wanted Visu

        '/api?key=:key&id=:id&lang=:lang&version=:version' GET

        Args:
            id: The unique ID of the Visu
            lang: The language code wanted for the Visu
            version: Use a specific version of our API
        """
        body = options['query'] if 'query' in options else {}
        body['id'] = id
        body['lang'] = lang
        body['version'] = version

        response = self.client.get('/api?key=' + self.key + '&id=' + id + '&lang=' + lang + '&version=' + version + '', body, options)

        return response

