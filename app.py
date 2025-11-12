import os
import sys
from datetime import timedelta
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS

# Carrega variáveis do .env
load_dotenv()

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.config.data_base import init_db, bcrypt, db
from src.routes import init_routes


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configurações do JWT
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key-default")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

    jwt = JWTManager(app)

    # Inicializações
    bcrypt.init_app(app)
    init_db(app)
    init_routes(app)

    # ✅ Rota raiz de status (para o Render não mostrar 404)
    @app.route("/")
    def home():
        return jsonify({
            "status": "API de Gestão de Estoque rodando com sucesso!",
            "versao": "1.0",
            "autor": "Alison Alencar"
        }), 200

    return app


# Instancia o app
app = create_app()

# Comando para inicializar o banco manualmente
@app.cli.command("init-db")
def init_db_command():
    """Cria as tabelas do banco de dados."""
    with app.app_context():
        db.create_all()
    print("✅ Banco de dados inicializado e tabelas criadas.")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
