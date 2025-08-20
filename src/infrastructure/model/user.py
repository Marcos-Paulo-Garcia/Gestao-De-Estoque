from src.config.data_base import db
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(18), unique=True, nullable=True)
    number = db.Column(db.String(15), nullable=True)
    status = db.Column(db.String(20), default="inactive", nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "CNPJ": self.cnpj,
            "number": self.number,
            "status": self.status
        }