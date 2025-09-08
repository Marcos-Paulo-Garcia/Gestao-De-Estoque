from flask import request, jsonify, make_response
from src.application.service.user_service import UserService
from src.config.data_base import db



class UserController:
    @staticmethod
    def register_user():
        try:
            data = request.get_json()
            if not data:
                return make_response(jsonify({"erro": "Dados JSON necessários"}), 400)
                
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            cnpj = data.get('cnpj')
            number = data.get('number')

            if not name or not email or not password:
                return make_response(jsonify({"erro": "Missing required fields"}), 400)
            
            user = UserService.create_user(name, email, password, cnpj, number)
            return make_response(jsonify({
                "mensagem": "User salvo com sucesso",
                "usuario": user.to_dict()
            }), 201)
        
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

    @staticmethod
    def get_user(idUser):
        try:
            user = UserService.get_user(idUser)
            if not user:
                return {"erro": "Usuário não encontrado"}, 404
            return make_response(jsonify({
                "usuario": user.to_dict()
            }), 200)
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

    @staticmethod
    def update_user(idUser):
        try:
            new_data = request.get_json()
            user = UserService.update_user(idUser, new_data)

            if not user:
                return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
            
            if user == "missing_fields":
                return make_response(jsonify({"erro": "Dados faltantes"}), 400)

            return make_response(jsonify({
                "mensagem": "User atualizado comsucesso",
                "usuario": user.to_dict()
            }), 200)
        
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

    @staticmethod
    def delete_user(idUser):
        try:
            user = UserService.delete_user(idUser)
            if not user:
                return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
            return make_response(jsonify({"mensagem": "Usuário deletado!"}), 200)
        
        except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

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