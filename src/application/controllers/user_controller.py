from flask import request, jsonify, make_response
from src.application.service.user_service import UserService
from src.config.data_base import db



class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        cnpj = data.get('cnpj')
        number = data.get('number')

        if not name or not email or not password or not cnpj or not number:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)
        
        user = UserService.create_user(name, email, password, cnpj, number)
        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 200)

    @staticmethod
    def get_user(idUser):
        user = UserService.get_user(idUser)
        if not user:
            return {"erro": "Usuário não encontrado"}, 404
        return make_response(jsonify({
            "usuario": user.to_dict()
        }), 200)

    @staticmethod
    def update_user(idUser):
        new_data = request.get_json()
        user = UserService.update_user(idUser, new_data)
        if not user:
            return{"erro": "Usuário não encontrado"}, 404
        
        if user == "missing_fields":
            return {"erro": "Dados faltantes"}, 400

        return make_response(jsonify({
            "mensagem": "User atualizado comsucesso",
            "usuarios": user.to_dict()
        }), 200)

    @staticmethod
    def delete_user(idUser):
        user = UserService.delete_user(idUser)
        if not user:
            return {"erro": "Usuário não encontrado"}, 404
        return {"mensagem": "Usuário deletado!"}, 200

  # --- MÉTODOS FALTANTES ---

    @staticmethod
    def activate_user():
        # Endpoint para o usuário enviar o código de ativação
        # Deverá receber o e-mail/id do usuário e o código
        pass

    @staticmethod
    def login():
        # Endpoint para autenticação do usuário (gerar token JWT)
        # Deverá verificar se o usuário está ativo
        pass