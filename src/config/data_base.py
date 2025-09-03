from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def init_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:root@mysql57:3306/market_management'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)