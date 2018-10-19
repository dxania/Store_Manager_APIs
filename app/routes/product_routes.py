from flask import Flask, jsonify, request

from Store_Manager_APIs.app import app

from Store_Manager_APIs.app.models.product_models import Product


a_product = Product()

@app.route('/')
def index():
    return "hey"


@app.route('/api/v1/products', methods = ['GET'])
def get_products():
    all_products = a_product.get_all_products()
    if all_products:
        return jsonify({"Products": all_products}), 200
    return jsonify({"Message":"There are no products in the store"}), 204


@app.route('/api/v1/products/<int:product_id>', methods = ['GET'])
def get_product(product_id):
    a_single_product = a_product.get_a_product(product_id)
    if a_product:
        return jsonify({"Product":a_single_product}), 200
    return jsonify({"Message":"There is no product matching that ID"}), 404


@app.route('/api/v1/products', methods =['POST'])
def create_product():
    data = request.json()
    
    product_id = data['product_id']
    product_name = data['product_name']
    model_no = data['model_no']
    product_category = data['product_category']
    unit_price = data['unit_price']
    product_quantity = data['product_quantity']
    
    created_product = a_product.created_a_product(product_name, model_no, product_category, unit_price, product_quantity)
    
    if created_product.create_product():
        return products.append(request.get_json()), 201
    else:
        return "nothing added"