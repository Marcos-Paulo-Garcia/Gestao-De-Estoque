from src.application.controllers.user_controller import UserController
from flask import jsonify, make_response

def init_routes(app):
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up"
        }), 200)

    @app.route('/user/:id', methods= ['GET'] )
    def get_user():
        return UserController.get_user()
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    
    @app.route('/user/:id', methods=['PUT'])
    def update_user():  
        return UserController.update_user()
    

    @app.route('/user/:id', methods= ['DELETE'] )
    def delete_user():
        return UserController.delete_user()