from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'postgresql+psycopg2://market_management_user:pjHE4fCG1m9EMRHXYl4qMiNx7N2lpysy@dpg-d4985g24d50c73969tdg-a/market_management?sslmode=require'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    print("✅ Banco conectado com sucesso!")
