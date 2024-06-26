# root __init__.py

import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view='authentication.do_login_user'
login_manager.session_protection='strong'
bcrypt = Bcrypt()

def create_app(config_Type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_Type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    from app.auth.models import User  # Import User model here

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
