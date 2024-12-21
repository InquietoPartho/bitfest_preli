from flask import Blueprint, jsonify
import os

recipes_bp = Blueprint('recipes', __name__)

# Read recipes from the file
def read_recipes():
    with open('my_fav_recipes.txt', 'r') as file:
        recipes = file.read().split('###')
    return recipes

# Get recipes based on available ingredients
@recipes_bp.route('/recipes', methods=['GET'])
def get_recipes():
    ingredients = request.args.get('ingredients').split(',')
    recipes = read_recipes()
    
    matching_recipes = []
    
    for recipe in recipes:
        if all(ingredient.lower() in recipe.lower() for ingredient in ingredients):
            matching_recipes.append(recipe.strip())
    
    return jsonify({"recipes": matching_recipes})
