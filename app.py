from flask import Flask
from flask_cors import CORS
# from flask_migrate import Migrate, MigrateCommand

# from src.controller.database import Base
from src.controller.database.database import SessionLocal, engine, init_db
from sqlalchemy.orm import scoped_session

from src.view.hello import blueprint_hello
from src.view.routes_v1 import blueprint_v1

import config

def create_app():
    app = Flask(__name__) 
    app.config.from_object('config.DevelopmentConfig')
    CORS(app)
    app.session = scoped_session(SessionLocal)

    return app

app = create_app()
app.register_blueprint(blueprint_hello, url_prefix='/hello')
app.register_blueprint(blueprint_v1, url_prefix='/v1')

init_db()

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)