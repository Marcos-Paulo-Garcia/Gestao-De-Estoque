from flask import Flask
from src.config.data_base import init_db
from src.routes import init_routes
from src.config.data_base import bcrypt

def create_app():
    app = Flask(__name__)

    bcrypt.init_app(app)
    init_db(app)

    init_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)