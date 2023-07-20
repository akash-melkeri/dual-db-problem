from flask import Blueprint, jsonify, session
from models import Admin, User

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login')
def login():
    print('login')
    # admin = Admin.objects().first()
    session['organization'] = 'test1'
    print(session,123123)
    user = User()
    user.user_name = 'raju1'
    user.save()
 
    return jsonify(ok=True)

@bp.route('/login2')
def login2():
    print('login2')
    # admin = Admin()
    # admin.user_name = 'test2'
    # admin.email = 'test2@gma.com'
    # admin.organization = 'test2'
    # admin.save()
    # session['organization'] = admin.organization
    session['organization'] = 'test2'
    print(session,99999)

    user = User()
    user.user_name = 'raju2'
    user.save()
 
    return jsonify(ok=True)

