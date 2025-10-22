import os
import sys
from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# Carrega as variáveis de ambiente ANTES de qualquer outra importação do projeto
load_dotenv()

# Adiciona a raiz do projeto ao sys.path para resolver os imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from src.config.data_base import init_db, bcrypt, db, SQLAlchemy
from src.routes import init_routes

def create_app():
    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key-default")

    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

    jwt = JWTManager(app)

    bcrypt.init_app(app)
    init_db(app)
    init_routes(app)

    return app

app = create_app()

@app.cli.command("init-db")
def init_db_command():
    """Cria as tabelas do banco de dados."""
    with app.app_context():
        db.create_all()
    print("Banco de dados inicializado e tabelas criadas.")


if __name__ == '__main__':
    app.run(debug=True)
