from src.infrastructure.model.product_model import Product
from src.infrastructure.model.sale_model import Sale
from src.infrastructure.model.user_model import User
from src.config.data_base import db

class SaleService:
    @staticmethod
    def register_sale(product_id, quantity, seller_id):
        try:
            # Verifica se o vendedor existe e está ativo
            seller = User.query.get(seller_id)
            if not seller or seller.status != "active":
                return None, "Vendedor não autorizado ou inativo.", 403

            # Busca o produto
            product = Product.query.get(product_id)
            if not product:
                return None, "Produto não encontrado.", 404

            # ❌ Removido: verificação de propriedade do produto
            # if product.seller_id != seller_id:
            #     return None, "Não autorizado. Este produto pertence a outro vendedor.", 403

            # Verifica se o produto está ativo
            if product.status != "active":
                return None, "Produto inativo não pode ser vendido.", 400

            # Verifica se há estoque suficiente
            if product.quantity < quantity:
                return None, f"Estoque insuficiente. Quantidade disponível: {product.quantity}", 409

            # Atualiza o estoque
            product.quantity -= quantity

            # Cria a venda (usa user_id, conforme seu Sale model)
            new_sale = Sale(
                product_id=product_id,
                user_id=seller_id,
                quantity=quantity,
                price_at_sale=product.price
            )

            db.session.add(new_sale)
            db.session.commit()

            # Retorna a venda criada e o status HTTP 201
            return new_sale, None, 201

        except Exception as e:
            db.session.rollback()
            return None, f"Erro ao registrar venda: {str(e)}", 500

    @staticmethod
    def get_sales(seller_id):
        try:
            # Busca todas as vendas do vendedor (user_id)
            sales = Sale.query.filter_by(user_id=seller_id).all()
            return sales
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao buscar vendas: {str(e)}")
