from flask import request, jsonify, Response

from app import app

from app.models.product_models import *

from ..models.product_models import Product


a_product = Product()

@app.route('/')
def index():
    return '<a href="https://store-manager-apis.herokuapp.com/api/v1/products">Navigate to this link to interact with the products endpoint</a>'


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

    input_d = request.get_json(force=True)

    pdt_name = input_d.get("product_name")
    if not pdt_name or pdt_name.isspace():
        return jsonify({"Message":"Product Name is required"}), 400

    pdt_model = input_d.get("model_no")
    if not pdt_model or pdt_model.isspace():
        return jsonify({"Message":"Product Model is required"}), 400

    pdt_category = input_d.get("product_category")
    if not pdt_category or pdt_category.isspace():
        return jsonify({"Message":"Product Category is required"}), 400
    
    pdt_price = input_d.get("unit_price")
    if not pdt_price :
        return jsonify({"Message":"Product Price is required"}), 400

    pdt_quantity = input_d.get("product_quantity")
    if not pdt_quantity:
        return jsonify({"Message":"Product Quantity is required"}), 400


    product={
            "product_id": len(products) + 1,
            "product_name" : pdt_name,
            "model_no" : pdt_model,
            "product_category": pdt_category,
            "unit_price": pdt_price,
            "product_quantity": pdt_quantity      
    }
    
    products.append(product)
    if products:
        return jsonify({"Added Product": product,"Message":"Product added successfully"}), 201
    else:
        return jsonify({"Message":"Insertion failed"}), 404