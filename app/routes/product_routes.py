from flask import request, jsonify, Response

from Store_Manager_APIs.app import app

from Store_Manager_APIs.app.models.product_models import *

from ..models.product_models import Product


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


# @app.route('/api/v1/products', methods =['POST'])
# def create_product():
    
#     input_d = request.get_json(force=True)
    
#     product={
#             'product_id': len(products) + 1,
#             'product_name' : input_d.get("product_name")
#             'model_no' : input_d.get('model_no'),
#             'product_category': input_d.get('product_category'),
#             'unit_price': input_d.get('unit_price'),
#             'product_quantity': input_d.get('product_quantity')      
#     }

#     if products.append(product):
#         return jsonify({"Added Product": product,"Message":"Product added successfully"}), 201, {'Content-Type': 'application/json'}
#     else:
#         return jsonify({"Message":"Insertion failed"}), 404
  
    







    # data_q = request.json

    # created_product = [Product.create_a_product(data_q['product_id'], data_q['product_name'], 
    #                                              data_q['model_no'], data_q('product_category'), 
    #                                              data_q['unit_price'], data_q['product_quantity'])



    # product_id = data_q['product_id']
    # product_name =data_q['product_name']
    # model_no = data_q['model_no']
    # product_category = data_q['product_category']
    # unit_price = data_q['unit_price']
    # product_quantity = data_q['product_quantity']
        #  product={
        #     'product_id': product_id,
        #     'product_name':product_name,
        #     'model_no' : model_no,
        #     'product_category': product_category,
        #     'unit_price': unit_price,
        #     'product_quantity': product_quantity      
        # }
    
    # if created_product:


    
    