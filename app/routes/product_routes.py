from flask import flash, request, jsonify

import json

from app import app

from app.models.product_models import *

from ..models.product_models import Product


a_product = Product()
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return """
    Products ==>
    <a href="https://store-manager-apis.herokuapp.com/api/v1/products">Navigate to this link to interact with the products endpoint</a><br><br>
    Sales ==>
    <a href="https://store-manager-apis.herokuapp.com/api/v1/sales">Navigate to this link to interact with the sales endpoint</a>
    """


@app.route('/api/v1/products', methods = ['GET'])
def get_products():
    all_products = a_product.get_all_products()
    if all_products:
        return jsonify({"Products": all_products}), 200
    else:
        return jsonify({
            "Message":"There are no products in the store"
        }), 404
    

@app.route('/api/v1/products/<int:product_id>', methods = ['GET'])
def get_product(product_id):
    a_single_product = a_product.get_a_product(product_id)
    if a_single_product:
        return jsonify({"Product":a_single_product}), 200
    return jsonify({
        "Message":"There is no product matching that ID"
    }), 404


@app.route('/api/v1/products', methods =['POST'])
def create_product():

    input_d = request.get_json(force=True)

    pdt_name = input_d.get("product_name")
    if not pdt_name or pdt_name.isspace():
        return jsonify({
            "Message":"Product Name is required"
        }), 400

    pdt_model = input_d.get("model_no")
    if not pdt_model or pdt_model.isspace():
        return jsonify({
            "Message":"Product Model is required"
        }), 400

    pdt_category = input_d.get("product_category")
    if not pdt_category or pdt_category.isspace():
        return jsonify({
            "Message":"Product Category is required"
        }), 400
    
    pdt_price = input_d.get("unit_price")
    if not pdt_price :
        return jsonify({
            "Message":"Product Price is required"
        }), 400

    pdt_quantity = input_d.get("product_quantity")
    if not pdt_quantity:
        return jsonify({
            "Message":"Product Quantity is required"
        }), 400

    product_id = len(a_product.products) + 1

    product = a_product.create_a_product(product_id,pdt_name,pdt_model,pdt_category,pdt_price,pdt_quantity)
    a_product.products.append(product)
    if a_product.products:
        return product, 201
    else:
        return jsonify({
            "Message":"Insertion failed"
        }), 400