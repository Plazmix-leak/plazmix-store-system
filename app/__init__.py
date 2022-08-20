import os
from flask import Flask
from flask_migrate import Migrate
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from app.helpers.database import RetryingQuery

BASE_DIRECTORY = os.getcwdb().decode("utf-8")


redis_client = FlaskRedis()
db = SQLAlchemy(query_class=RetryingQuery)

migrate = Migrate()

app = Flask(__name__, static_folder=os.path.join(BASE_DIRECTORY, "static"),
            template_folder=os.path.join(BASE_DIRECTORY, "templates"))
app.config.from_object(os.getenv('FLASK_ENV') or 'config.Production')


db.init_app(app)
redis_client.init_app(app)
migrate.init_app(app, db)
