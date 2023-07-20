from flask import Flask, session, request
from views import bp as views_bp
from utils import JSONEncoder, verify_token, unhandled_exception
from mongoengine import connect
from models import User

app = Flask(__name__)

app.config.from_pyfile('config.py')
app.json_encoder = JSONEncoder

main_db_connection = connect(alias='main',db=app.config['MONGO_DBNAME'],host=app.config['MONGODB_URI'])
# sub_db_connection = connect(db=app.config['MONGO_DBNAME'])

connections = {}

def before_request():
    print('before request: ')
    print(connections)
    print(session)
    # sub_db_connection.get_database(session.get('organization'))
    if(session.get('organization')):
        if(session.get('organization') not in connections):
            connections[session.get('organization')] = connect(db=session.get('organization'))
        connections[session.get('organization')].get_database(session.get('organization'))
    
    # if(session.get('organization')):
    #     if(session.get('organization') not in connections):
    #         connections[session.get('organization')] = connect(db=session.get('organization'))
    #     connections[session.get('organization')].get_database(session.get('organization'))
    

app.before_request(before_request)

app.errorhandler(unhandled_exception)
app.register_blueprint(views_bp)

if __name__ == '__main__':
    app.run(port=6001)