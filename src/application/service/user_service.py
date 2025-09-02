from src.domain.user import UserDomain
from src.infrastructure.model.user_model import User
from src.config.data_base import db
from src.infrastructure.http.whats_app import WhatsApp

class UserService:
    @staticmethod
    def create_user(name, email, password, cnpj, number):
        new_user = UserDomain(name, email, password, cnpj, number)
        code = WhatsApp.sendMenssage()
        user = User(name=new_user.name, email=new_user.email, password=new_user.password, cnpj=new_user.cnpj, number=new_user.number, code = code)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user(idUser):
        user = User.query.get(idUser)
        if not user:
            return None
        return user
    @staticmethod
    def update_user(idUser, new_data):
        user = User.query.get(idUser)
        if not user:
            return None
        
        required_fields = ['name', 'email', 'password', 'cnpj', 'number']
        if not all(field in new_data and new_data[field] not in [None, ""] for field in required_fields):
            return "missing_fields"
        
        user.name = new_data["name"]
        user.email = new_data["email"]
        user.password = new_data["password"]
        user.cnpj = new_data["cnpj"]
        user.number = new_data["number"]

        db.session.commit()
        return user
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        db.session.delete(user)
        db.session.commit()
        return user