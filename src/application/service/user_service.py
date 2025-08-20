from src.domain.user import UserDomain
from src.infrastructure.model.user import User
from src.config.data_base import db

class UserService:
    @staticmethod
    def create_user(name, email, password, cnpj, number):
        new_user = UserDomain(name, email, password, cnpj, number)
        user = User(name=new_user.name, email=new_user.email, password=new_user.password, cnpj=new_user.cnpj, number=new_user.number)
        db.session.add(user)
        db.session.commit()
        return user