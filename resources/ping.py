from flask import request
from flask_restful import Resource
import requests


class PingAPI(Resource):
    def post(self):
        try:
            url = request.json.get('url', None)

            if url is None:
                return {'status': False, 'message': 'URL key is required'}, 400

            if len(url) == 0:
                return {'status': False, 'message': 'URL key value is required'}, 400

            if self.is_valid_url(url):
                response = self.get_payload_data('GET', url)
                if response.status_code == 200:
                    response_data = response.json().get('data')

                    response = {
                                   'status': True,
                                   'message': 'Payload data loaded successfully',
                                   'data': response_data
                               }, 200

                    return response
            else:
                return {'status': False, 'msg': 'Invalid URL Pattern'}, 400
        except Exception as e:
            return {'status': False, 'message': str(e)}, 500

    @staticmethod
    def is_valid_url(url):
        import re
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and regex.search(url)

    @staticmethod
    def get_payload_data(method, url):
        payload = {}
        headers = {
            'Authorization': 'BEARER_TOKEN'
        }
        response = requests.request(method, url, headers=headers, data=payload)

        return response
