from flask_restful import Resource


class InfoAPI(Resource):
    def get(self):
        response = {
                       'Receiver': 'Cisco is the best!',
                   }, 200

        return response
