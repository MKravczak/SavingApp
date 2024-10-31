from flask import Blueprint, request, jsonify  # Import necessary modules from Flask
from .models import User, Transaction, Category, Product  # Import models
from . import db  # Import the database instance

main = Blueprint('main', __name__)  # Create a Blueprint named 'main'

# === User ===

# Add a new user
@main.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()  # Get JSON data from the request
    new_user = User(username=data['username'], monthly_limit=data['monthly_limit'])  # Create a new User instance
    db.session.add(new_user)  # Add the new user to the session
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'User added'}), 201  # Return a success message

# Get a user by ID
@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)  # Query the user by ID or return 404 if not found
    return jsonify(user.to_json())  # Return user details as JSON

# Update a user
@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)  # Query the user by ID or return 404 if not found
    data = request.get_json()  # Get JSON data from the request
    user.username = data.get('username', user.username)  # Update the username if provided
    user.monthly_limit = data.get('monthly_limit', user.monthly_limit)  # Update the monthly limit if provided
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'User updated'})  # Return a success message

# Delete a user
@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)  # Query the user by ID or return 404 if not found
    db.session.delete(user)  # Delete the user from the session
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'User deleted'})  # Return a success message

# === Transactions ===

# Add a new transaction
@main.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()  # Get JSON data from the request
    new_transaction = Transaction(
        user_id=data['user_id'],
        category_id=data['category_id'],
        product_id=data.get('product_id'),
        amount=data['amount'],
        description=data.get('description')
    )  # Create a new Transaction instance
    db.session.add(new_transaction)  # Add the new transaction to the session
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'Transaction added'}), 201  # Return a success message

# Get all transactions for a user
@main.route('/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    transactions = Transaction.query.filter_by(user_id=user_id).all()  # Query all transactions for the user
    return jsonify(list(map(lambda trans: trans.to_json(), transactions)))  # Return the list as JSON

# Update a transaction
@main.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)  # Query the transaction by ID or return 404 if not found
    data = request.get_json()  # Get JSON data from the request
    transaction.amount = data.get('amount', transaction.amount)  # Update the amount if provided
    transaction.description = data.get('description', transaction.description)  # Update the description if provided
    transaction.category_id = data.get('category_id', transaction.category_id)  # Update the category ID if provided
    transaction.product_id = data.get('product_id', transaction.product_id)  # Update the product ID if provided
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'Transaction updated'})  # Return a success message

# Delete a transaction
@main.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)  # Query the transaction by ID or return 404 if not found
    db.session.delete(transaction)  # Delete the transaction from the session
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'Transaction deleted'})  # Return a success message

# === Products ===

# Add a new product
@main.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()  # Get JSON data from the request
    new_product = Product(name=data['name'], price=data['price'])  # Create a new Product instance
    db.session.add(new_product)  # Add the new product to the session
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'Product added'}), 201  # Return a success message

# Get all products
@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()  # Query all products
    return jsonify(list(map(lambda product: product.to_json(), products)))  # Return the list as JSON

# === Categories ===

# Add a new category
@main.route('/categories', methods=['POST'])
def add_category():
    data = request.get_json()  # Get JSON data from the request
    new_category = Category(name=data['name'])  # Create a new Category instance
    db.session.add(new_category)  # Add the new category to the session
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'Category added'}), 201  # Return a success message

# Get all categories
@main.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()  # Query all categories
    return jsonify(list(map(lambda category: category.to_json(), categories)))  # Return the list as JSON

# Update a category
@main.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)  # Query the category by ID or return 404 if not found
    data = request.get_json()  # Get JSON data from the request
    category.name = data.get('name', category.name)  # Update the name if provided
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'Category updated'})  # Return a success message

# Delete a category
@main.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)  # Query the category by ID or return 404 if not found
    db.session.delete(category)  # Delete the category from the session
    db.session.commit()  # Commit the session to the database
    return jsonify({'message': 'Category deleted'})  # Return a success message