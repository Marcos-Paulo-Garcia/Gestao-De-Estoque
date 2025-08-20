from flask import request, jsonify, make_response
from src.application.service.user_service import UserService

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
