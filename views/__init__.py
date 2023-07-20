from flask import Blueprint

bp = Blueprint('views', __name__)
from views import auth, user

bp.register_blueprint(auth.bp, url_prefix='/api/auth')
bp.register_blueprint(user.bp, url_prefix='/api/user')