from flask import Flask
from routes.ingredients import ingredients_bp
from routes.recipes import recipes_bp
from routes.chatbot import chatbot_bp
from models.ingredients import create_db

app = Flask(__name__)

# Call create_db to initialize the database and table
create_db()

app.register_blueprint(ingredients_bp, url_prefix='/api')
app.register_blueprint(recipes_bp, url_prefix='/api')
app.register_blueprint(chatbot_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
