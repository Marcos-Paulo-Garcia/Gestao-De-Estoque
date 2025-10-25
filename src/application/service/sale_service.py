from src.domain.sale import SaleDomain
from src.infrastructure.model.product_model import Product
from src.infrastructure.model.sale_model import Sale
from src.infrastructure.model.user_model import User
from src.config.data_base import db

class SaleService:
  @staticmethod
  def register_sale(product_id, quantity, seller_id):
    seller = User.query.get(seller_id)
    if not seller or seller.status != 'active':
        return None, "Vendedor não autorizado ou inativo.", 403

    product = Product.query.get(product_id)

    if not product:
        return None, "Produto não encontrado", 404
    
    if product.seller_id != seller_id:
        return None, "Não autorizado. Este produto pertence a outro vendedor.", 403

    if product.status != 'active':
        return None, "Produto inativo não pode ser vendido.", 400

    if product.quantity < quantity:
        return None, f"Estoque insuficiente. Quantidade disponível: {product.quantity}", 409

    product.quantity -= quantity

    new_sale = Sale(
        product_id=product_id,
        seller_id=seller_id,
        quantity=quantity,
        price_at_sale=product.price
    )

    db.session.add(new_sale)
    db.session.commit()

    return new_sale, None, None

  @staticmethod
  def get_sales(seller_id):
    sales = Sale.query.filter_by(seller_id=seller_id).all()
    return sales