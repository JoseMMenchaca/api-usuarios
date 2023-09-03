from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()
migrate=Migrate()

def create_app(config_name='config'):
    app = Flask(__name__)
    app.config.from_object(config_name)
    
    from app.models import Usuario
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from app.routes.app import bp

    app.register_blueprint(bp,url_prefix='/api/v1')
    return app