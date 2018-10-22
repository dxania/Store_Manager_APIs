from flask import Flask


app = Flask(__name__)

from Store_Manager_APIs.app.routes import product_routes
