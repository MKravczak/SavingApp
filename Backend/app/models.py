from datetime import datetime
from __init__ import db


class User(db.Model):
    __tablename__ = 'users'  # Table to store user information

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username of the user
    monthly_limit = db.Column(db.Float, nullable=False)  # Monthly spending limit for the user
    transactions = db.relationship('Transaction', backref='user', lazy=True)  # Relationship to transactions made by the user

    def __repr__(self):
        return f'<User {self.username}>'



class Category(db.Model):
    __tablename__ = 'categories'  # Table to store categories of transactions

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each category
    name = db.Column(db.String(50), unique=True, nullable=False)  # Name of the category
    transactions = db.relationship('Transaction', backref='category', lazy=True)  # Relationship to transactions under this category

    def __repr__(self):
        return f'<Category {self.name}>'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }



class Product(db.Model):
    __tablename__ = 'products'  # Table to store product information

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each product
    name = db.Column(db.String(100), unique=True, nullable=False)  # Name of the product
    price = db.Column(db.Float, nullable=False)  # Price of the product
    transactions = db.relationship('Transaction', backref='product', lazy=True)  # Relationship to transactions involving this product

    def __repr__(self):
        return f'<Product {self.name} - {self.price}>'

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'monthly_limit': self.monthly_limit
        }




class Transaction(db.Model):
    __tablename__ = 'transactions'  # Table to store transaction details

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each transaction
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to the user who made the transaction
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)  # Foreign key to the category of the transaction
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)  # Foreign key to the product involved in the transaction (if any)
    amount = db.Column(db.Float, nullable=False)  # Amount of money involved in the transaction
    description = db.Column(db.String(200))  # Description of the transaction
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of when the transaction occurred
    month = db.Column(db.Integer)  # Month of the transaction
    year = db.Column(db.Integer)  # Year of the transaction

    def __repr__(self):
        return f'<Transaction {self.amount} - {self.timestamp}>'

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'product_id': self.product_id,
            'amount': self.amount,
            'description': self.description,
            'timestamp': self.timestamp,
            'month': self.month,
            'year': self.year
        }