from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
 
bcrypt = Bcrypt()

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:mpfg2005@localhost:3306/market_management' #MUDAR A MINHA SENHA
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)