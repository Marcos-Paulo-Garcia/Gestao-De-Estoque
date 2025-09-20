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
    
<<<<<<< Updated upstream
    
    @app.route('/user/:id', methods=['PUT'])
    def update_user():  
        return UserController.update_user()
=======
    @app.route('/user/<int:id>', methods=['PUT'])
    def update_user(id):  
        return UserController.update_user(id)
>>>>>>> Stashed changes
    
    @app.route('/user/<int:id>/inativar', methods= ['PUT'] )
    def inativar_user(id):
        return UserController.inativar_user(id)

<<<<<<< Updated upstream
    @app.route('/user/:id', methods= ['DELETE'] )
    def delete_user():
        return UserController.delete_user()
=======
    @app.route('/user/ativar', methods=['POST'])
    def ativar_user():
        return UserController.ativar_user()
    
    @app.route('/login', methods= ['POST'])
    def login():
        return UserController.login()
>>>>>>> Stashed changes
