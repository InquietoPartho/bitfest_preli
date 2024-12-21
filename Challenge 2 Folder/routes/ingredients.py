from flask import Blueprint, request, jsonify
import sqlite3

ingredients_bp = Blueprint('ingredients', __name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('database/db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

# Add new ingredient
@ingredients_bp.route('/ingredients', methods=['POST'])
def add_ingredient():
    data = request.json
    name = data.get('name')
    quantity = data.get('quantity')
    
    conn = get_db_connection()
    conn.execute('INSERT INTO ingredients (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Ingredient added successfully!"}), 201

# Update ingredient
@ingredients_bp.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredient(id):
    data = request.json
    name = data.get('name')
    quantity = data.get('quantity')
    
    conn = get_db_connection()
    conn.execute('UPDATE ingredients SET name = ?, quantity = ? WHERE id = ?', (name, quantity, id))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Ingredient updated successfully!"})

# Get all ingredients
@ingredients_bp.route('/ingredients', methods=['GET'])
def get_ingredients():
    conn = get_db_connection()
    ingredients = conn.execute('SELECT * FROM ingredients').fetchall()
    conn.close()
    
    ingredients_list = [{"id": ingredient["id"], "name": ingredient["name"], "quantity": ingredient["quantity"]} for ingredient in ingredients]
    return jsonify(ingredients_list)
