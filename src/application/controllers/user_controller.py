from flask import request, jsonify, make_response
from src.application.service.user_service import UserService
from config.data_base import db


class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        cnpj = data.get('CNPJ')
        number = data.get('number')

        if not name or not email or not password or not cnpj or not number:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)
        
        user = UserService.create_user(name, email, password, cnpj, number)
        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 200)




    def get_user(idUser):
        user = db.session.get(UserController, idUser)
        return user.to_dict() if user else {"erro": "Usuário não encontrado"}





    def update_user(idUser, new_data):
        user = db.session.get (UserController, idUser)
        if not user:
            return{"erro": "Usuário não encontrado"}, 404
        
        required_fields = ['name', 'email', 'password', 'cnpj', 'number']
        if not all(fields in new_data and new_data[fields] not in [None, ""] for fields in required_fields):
            return {"erro": "Todos os campos são obrigatórios!"}, 400

        user.name = new_data["name"]
        user.email = new_data["email"]
        user.password = new_data["password"]
        user.cnpj = new_data["cnpj"]
        user.number = new_data["number"]

        db.session.commit()

        return {"mensagem": "Usuário atualizado!"}