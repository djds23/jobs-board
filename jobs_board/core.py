from flask import Flask
from flask.ext.foundation import Foundation
from flask.ext.mail import Mail
from flask_security import Security, SQLAlchemyUserDatastore
from flask.ext.sqlalchemy import SQLAlchemy
from jobs_board.forms import ExtendedRegisterForm

db = SQLAlchemy()
foundation = Foundation()
mail = Mail()
security = Security()

def create_app():
    app = Flask(__name__)
    app.config.from_object('jobs_board.settings')
    db.init_app(app)
    foundation.init_app(app)
    mail.init_app(app)
    from .users.models import Role, User
    security.init_app(
        app,
        SQLAlchemyUserDatastore(db, User, Role),
        register_form=ExtendedRegisterForm,
    )
    from .jobs.views import blueprint as jobs
    app.register_blueprint(jobs)
    return app
