from datetime import datetime
from src.db import db


class Category(db.Model):
    """
    Category
    """
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name


class Product(db.Model):
    """
    Product
    """
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    vendor = db.Column(db.String(50), nullable=False)
    price = db.Column(db.DECIMAL)
    admissible_region = db.Column(db.String(50), nullable=False)

    def __init__(self, product_id, product_name, description, image, vendor, price, admissible_region):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.image = image
        self.vendor = vendor
        self.price = price
        self.admissible_region = admissible_region


class ProductCategory(db.Model):
    """
    Product Category
    """
    __tablename__ = 'product_category'
    __table_args__ = {'extend_existing': True}
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, category_id, product_id):
        self.category_id = category_id
        self.product_id = product_id
