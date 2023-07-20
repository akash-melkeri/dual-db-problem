from flask import Flask, session, request
from views import bp as views_bp
from utils import JSONEncoder, verify_token, unhandled_exception
from mongoengine import connect, disconnect
from mongoengine.connection import get_connection
from models import User
from pprint import pprint

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.json_encoder = JSONEncoder

main_db_connection = connect(alias='main',db=app.config['MONGO_DBNAME'],host=app.config['MONGODB_URI'])
# sub_db_connection = connect(db=app.config['MONGO_DBNAME'])

connections = {}

def before_request():
    if(session.get('organization')):
        connect(db=session.get('organization'))

def after_request(val):
    if(session.get('organization')):
        disconnect()

app.before_request(before_request)
app.teardown_request(after_request)

app.errorhandler(unhandled_exception)
app.register_blueprint(views_bp)

if __name__ == '__main__':
    app.run(port=6001)