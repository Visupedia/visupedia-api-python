class ResponseHandler(object):

    """ResponseHandler takes care of decoding the response body into suitable type"""

    @staticmethod
    def get_body(response):
        typ = response.headers.get('content-type')
        body = response.text

        return body
