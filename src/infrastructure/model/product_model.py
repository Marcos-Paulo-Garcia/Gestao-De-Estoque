from src.config.data_base import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(100), nullable=False)
    price = db.column(db.Float, nullable=False)
    quantity = db.column(db.Integer, nullable=False)
    status = db.column(db.String(20), default="inactive", nullable=False)
    image_url = db.column(db.String(255), nullable=True)
    seller_id = db.column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "status": self.status,
            "image_url": self.image_url,
            "seller_id": self.seller_id
        }
