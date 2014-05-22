from .http_client import HttpClient

# Assign all the api classes
from .api.visu import Visu


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def visu(self, key):
        """Returns an MyVisu api instance

        Args:
            key: The api key provided by Visupedia
        """
        return Visu(key, self.http_client)

