import datetime

from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from config.constant import *

from resources.ping import PingAPI
from resources.info import InfoAPI


app = Flask(__name__)
app.secret_key = APP_SECRET
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

CORS(app)

app.config['DEBUG'] = True

app.config['JWT_SECRET_KEY'] = JWT_SECRET
jwt = JWTManager(app)

api = Api(app, prefix='/api')


api.add_resource(PingAPI, '/ping', endpoint='ping', methods=["POST"])
api.add_resource(InfoAPI, '/info', endpoint='info', methods=["GET"])


@app.route('/')
def index():
    return "Welcome To Cisco"


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0")
