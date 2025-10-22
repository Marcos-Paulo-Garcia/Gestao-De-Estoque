from flask import request, jsonify, make_response
from src.application.service.product_service import ProductService
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProductController:
  @staticmethod
  @jwt_required()
  def register_product():
    try:
      data = request.get_json()
      if not data: 
        return make_response(jsonify({"erro": "Dados JSON necessários"}), 400)
      
      # Obtém os dados do corpo da requisição
      name = data.get('name')
      price = data.get('price')
      quantity = data.get('quantity')
      status = data.get('status', 'active') # Define 'active' como padrão se não for fornecido
      image_url = data.get('image_url')
      
      # Obtém o ID do vendedor a partir do token JWT
      seller_id = get_jwt_identity()
      
      # Validação dos campos obrigatórios
      required_fields = {'name': name, 'price': price, 'quantity': quantity}
      for field, value in required_fields.items():
          if value is None:
              return make_response(jsonify({"erro": f"O campo '{field}' é obrigatório"}), 400)
              
      product = ProductService.create_product(name, price, quantity, status, image_url, seller_id)
      return make_response(jsonify({
          "mensagem": "Produto criado com sucesso",
          "produto": product.to_dict()
      }), 201)
      
    except Exception as e:
      return make_response(jsonify({"erro": str(e)}), 500)
    
  @staticmethod
  @jwt_required()
  def get_products():
    try:
        seller_id = get_jwt_identity()
        products = ProductService.get_products(seller_id)
        if not products:
          return {"erro": "Não há produtos cadastrados"}, 404
        return make_response(jsonify({"produtos": [product.to_dict() for product in products]}), 200)
                             
    except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

  @staticmethod
  @jwt_required()
  def get_product_id(id):
    try: 
      current_seller_id = get_jwt_identity()
      product = ProductService.get_product_id(id)
      if not product:
          return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
      
      if str(product.seller_id) != str(current_seller_id):
        return make_response(jsonify({"erro": "Acesso não autorizado a este produto"}), 403)

      return make_response(jsonify({"produto": product.to_dict()}), 200)
    
    except Exception as e:
            return make_response(jsonify({"erro": str(e)}), 500)

  @staticmethod
  @jwt_required()
  def update_product(id):
    try:
      current_seller_id = get_jwt_identity()
      product = ProductService.get_product_id(id)

      if not product:
        return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

      # Verifica se o usuário logado é o dono do produto
      if str(product.seller_id) != str(current_seller_id):
        return make_response(jsonify({"erro": "Não autorizado. Você não é o vendedor deste produto."}), 403)

      data = request.get_json()
      if not data:
        return make_response(jsonify({"erro": "Dados JSON necessários para atualização"}), 400)

      updated_product = ProductService.update_product(id, data)

      return make_response(jsonify({
          "mensagem": "Produto atualizado com sucesso",
          "produto": updated_product.to_dict()
      }), 200)
    except Exception as e:
      return make_response(jsonify({"erro": str(e)}), 500)

  @staticmethod
  @jwt_required()
  def inativar_product(id):
    try:
      current_seller_id = get_jwt_identity()
      product = ProductService.get_product_id(id)

      if not product:
        return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

      # Verifica se o usuário logado é o dono do produto
      if str(product.seller_id) != str(current_seller_id):
        return make_response(jsonify({"erro": "Não autorizado. Você não é o vendedor deste produto."}), 403)

      inactivated_product = ProductService.inativar_product(id)

      return make_response(jsonify({
          "mensagem": "Produto inativado com sucesso",
          "produto": inactivated_product.to_dict()
      }), 200)
    except Exception as e:
      return make_response(jsonify({"erro": str(e)}), 500)
