from flask import Flask
from flask_cors import CORS
# from flask_migrate import Migrate, MigrateCommand

from src.controller.database import Base
from src.controller.database.database import SessionLocal, engine, init_db
from src.view.hello import blueprint
from sqlalchemy.orm import scoped_session
import config

Base.metadata.create_all(bind=engine)

def create_app():
    app = Flask(__name__) 
    app.config.from_object('config.DevelopmentConfig')
    CORS(app)
    app.session = scoped_session(SessionLocal)

    return app

app = create_app()
app.register_blueprint(blueprint, url_prefix='/hello')

init_db()

@app.teardown_appcontext
def remove_session(*args, **kwargs):
    app.session.remove()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)