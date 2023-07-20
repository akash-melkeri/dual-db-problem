from flask import Blueprint, jsonify
from models import Admin, User

bp = Blueprint('user', __name__, url_prefix='/api/user')

@bp.route('/users',methods=["GET"])
def get_users():
    print("users")
    return jsonify(ok=True)
