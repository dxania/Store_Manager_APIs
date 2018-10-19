from flask import request, jsonify, request

from Store_Manager_APIs.app import app

from Store_Manager_APIs.app.models.sales_models import Sales


a_sale = Sales()

@app.route('/')
def index():
    return "hey"


@app.route('/api/v1/sales', methods = ['GET'])
def get_sales():
    all_sales = a_sale.get_all_sales()
    if all_sales:
        return jsonify({"Products": all_sales}), 200
    return jsonify({"Message":"There are no sales yet"}), 204


@app.route('/api/v1/sales/<int:sales_id>', methods = ['GET'])
def get_sale(sales_id):
    a_single_sale = a_sale.get_sale(sales_id)
    if a_sale:
        return jsonify({"Product":a_single_sale}), 200
    return jsonify({"Message":"There is no sale record matching that ID"}), 404


@app.route('/api/v1/sales', methods =['POST'])
def create_sale():

    created_sale = a_sale.create_sale()
    
    if created_sale:
        return sales.append(request.get_json()), 201
    else:
        return jsonify({"Message","Insertion failed"}), 404

    
    