from flask import Flask


app = Flask(__name__)

from app.routes import product_routes
from app.routes import sales_routes
