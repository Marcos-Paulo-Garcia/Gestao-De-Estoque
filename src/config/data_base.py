<<<<<<< Updated upstream
from flask_sqlalchemy import SQLAlchemy 
=======
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt

brypt = Bcrypt()
>>>>>>> Stashed changes

db = SQLAlchemy()

def init_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@mysql57:3306/market_management'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)