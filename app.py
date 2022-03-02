import os
from flask import Flask
from flask_restful import Api
from seeder import add_dummy_data
from src.resources import AllProducts, AllCategories

# App Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'qwertyuiopasdfghjkl'
api = Api(app)

# Setup
@app.before_first_request
def create_tables():
    db.create_all()
    add_dummy_data()

# API Routes
api.add_resource(AllProducts, '/all_products')
api.add_resource(AllCategories, '/all_categories')

# MAIN
if __name__ == '__main__':
    from src.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
    # Delete DB (Teardown)
    if os.path.exists("data.db"):
        os.remove("data.db")
    else:
        pass
