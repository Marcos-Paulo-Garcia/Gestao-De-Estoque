from src.application.controllers.user_controller import UserController
from flask import jsonify, make_response

def init_routes(app):
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up"
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    #PRECISA CRIAR O "CORPO" DESSAS ROTAS
    @app.route('/user/:id', methods=['PUT'])
    def update_user():  
        return
    
    @@app.route('/user/:id', methods= ['GET'] )
    def get_user():
        return