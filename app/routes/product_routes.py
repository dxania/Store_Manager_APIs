from flask import flash, request
from flask import jsonify, make_response
import json

from app import app

from app.models.product_models import *


product_object = Product()


@app.route('/')
def index():
    """The first page and endpoint that 
    is rendered on loading the url
    """
    return """
    Products ==>
    <a href="https://store-manager-apis.herokuapp.com/api/v1/products">
    Navigate to this link to interact with the products endpoint</a><br><br>
    Sales ==>
    <a href="https://store-manager-apis.herokuapp.com/api/v1/sales">
    Navigate to this link to interact with the sales endpoint</a>
    """


@app.route('/api/v1/products', methods = ['GET'])
def get_products():
    """The retrieve all products function 
    wrapped around the Get /products endpoint
    """
    all_products = product_object.get_all_products()
    if all_products:
        return jsonify(all_products), 200
    else:
        return jsonify(
            {"Message":"There are no products in the store"
        }), 404
    

@app.route('/api/v1/products/<int:product_id>', methods = ['GET'])
def get_product(product_id):
    """The retrieve a particular product 
    function wrapped around the Get 
    /product/<int:product_id> endpoint
    """
    a_single_product = product_object.get_a_product(product_id)
    if a_single_product:
        return a_single_product, 200
    return jsonify({
        "Message":"There is no product matching that ID"
    }), 404


@app.route('/api/v1/products', methods =['POST'])
def create_product():
    """The create a product function 
    wrapped around the Post /products endpoint
    """
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

    product_id = len(product_object.products) + 1

    product = product_object.create_a_product(  product_id,
                                                pdt_name,pdt_model,
                                                pdt_category,pdt_price,
                                                pdt_quantity)

    product_object.products.append(product)
    if product_object.products:
        return product, 201
    else:
        return jsonify({
            "Message":"Insertion failed"
        }), 400
