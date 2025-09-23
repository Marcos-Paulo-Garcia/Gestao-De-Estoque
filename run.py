from datetime import timedelta
from flask import Flask
from src.config.data_base import init_db, bcrypt, db
from src.routes import init_routes
from flask_jwt_extended import JWTManager
import os

def create_app():
    app = Flask(__name__)

    # Chave secreta para JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key-default")

    # Expiração do token de acesso: 1 hora
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

    jwt = JWTManager(app)

    bcrypt.init_app(app)
    init_db(app)
    init_routes(app)

    return app

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
