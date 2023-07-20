from flask import Blueprint, jsonify, session
from models import Admin, User

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login/<string:user>')
def login(user):
    print('LOGIN')
    print(user)
    admin = Admin.objects(user_name=user).first()
    if(not admin):
        print('NEW ADMIN')
        admin = Admin()
        admin.user_name = user
        admin.email = user + '@gmail.com'
        admin.organization = 'org_' + user
        admin.save()
    print('session before ', session)
    session['organization'] = admin.organization
    print('session after ', session)
    
    return jsonify(ok=True)

@bp.route('/create_user/<string:user>')
def create_user(user):
    print('CREATE_USER')
    new_user = User()
    new_user.user_name = user
    new_user.save()
 
    return jsonify(ok=True)

