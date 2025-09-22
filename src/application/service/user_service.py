from src.domain.user import UserDomain
from src.infrastructure.model.user_model import User
from src.config.data_base import db , bcrypt
from src.infrastructure.http.whats_app import WhatsApp

class UserService:
    @staticmethod
    def create_user(name, email, password, cnpj, number):

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = UserDomain(name, email, hashed_password, cnpj, number)
        Whats=WhatsApp()
        code=Whats.send_code(to_number='whatsapp:+5511985478886')

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
        user.password = bcrypt.generate_password_hash(new_data["password"]).decode("utf-8")
        user.cnpj = new_data["cnpj"]
        user.number = new_data["number"]

        db.session.commit()
        return user
    @staticmethod
    def inativar_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        user.status = "inactive"
        db.session.commit()
        return user

    @staticmethod
    def ativar_user(email,code):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None, "Usuário não encontrado"

        if user.code != code:
            return None, "Código inválido"

        user.status = "active"
        db.session.commit()
        return user , None  

    @staticmethod
    def autenticacao(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None
        
        if not bcrypt.check_password_hash(user.password, password):
            return None
        
        if user.status != "active":
            return None
            
        return user