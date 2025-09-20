from flask import request, jsonify, make_response
from src.application.service.user_service import UserService
from src.config.data_base import db
from flask_jwt_extended import create_access_token, jwt_required


class UserController:
    @staticmethod
    def register_user():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        cnpj = data.get('cnpj')
        number = data.get('number')

<<<<<<< Updated upstream
        if not name or not email or not password or not cnpj or not number:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)
=======
            if not name or not email or not password or not cnpj or not number:
                return make_response(jsonify({"erro": "Missing required fields"}), 400)
            
            user = UserService.create_user(name, email, password, cnpj, number)
            return make_response(jsonify({
                "mensagem": "User salvo com sucesso",
                "usuario": user.to_dict()
            }), 201)
>>>>>>> Stashed changes
        
        user = UserService.create_user(name, email, password, cnpj, number)
        return make_response(jsonify({
            "mensagem": "User salvo com sucesso",
            "usuarios": user.to_dict()
        }), 200)

    @staticmethod
    @jwt_required()
    def get_user(idUser):
        user = UserService.get_user(idUser)
        if not user:
            return {"erro": "Usuário não encontrado"}, 404
        return make_response(jsonify({
            "usuario": user.to_dict()
        }), 200)

    @staticmethod
    @jwt_required()
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
<<<<<<< Updated upstream
    def delete_user(idUser):
        user = UserService.delete_user(idUser)
        if not user:
            return {"erro": "Usuário não encontrado"}, 404
        return {"mensagem": "Usuário deletado!"}, 200
=======
    def inativar_user(idUser):
        try:
            user = UserService.inativar_user(idUser)
            if not user:
                return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
            return make_response(jsonify({"mensagem": "Usuário inativado!"}), 200)
        
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)
>>>>>>> Stashed changes

  

    @staticmethod
    def ativar_user():
        try:
            data = request.get_json()
            email = data.get("email")
            code = data.get("code")

            user, erro = UserService.ativar_user(email,code)
            if erro:
                return make_response(jsonify({"erro": erro}), 400)

            return make_response(jsonify({
                "mensagem" : "Usuário ativado com sucesso",
                "usuario" : user.to_dict()
            }), 200)

        except Exception as e:
            return make_response(jsonify({"erro" : str(e)}), 500)
        

    @staticmethod
    def login():
        try:
            data = request.get_json()
            email = data.get("email")
            password = data.get("password")

            user = UserService.autenticacao(email, password)
            if not user:
                return make_response(jsonify({"erro": "Credenciais inválidas"}), 401)

            access_token = create_access_token(identity=user.id)

            return jsonify({
                "access_token": access_token,
                "usuario": user.to_dict()
            }), 200

        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)
