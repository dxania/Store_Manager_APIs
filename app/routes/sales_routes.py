from flask import request, jsonify, Response

from Store_Manager_APIs.app import app

from Store_Manager_APIs.app.models.sales_models import *

from ..models.sales_models import Sales

#instance of the Sales class
a_sale = Sales()

#endpoint for the index page
# @app.route('/')
# def index():
#     return "hey"

#GET /sales endpoint 
@app.route('/api/v1/sales', methods = ['GET'])
def get_sales():
    #use Sales instance a_sale to invoke get_all_sales function
    all_sales = a_sale.get_all_sales()
    if all_sales:
        return jsonify({"Products": all_sales}), 200
    return jsonify({"Message":"There are no sales yet"}), 204

#GET /sales/<int:sales_id> endpoint
@app.route('/api/v1/sales/<int:sales_id>', methods = ['GET'])
def get_sale(sales_id):
    #use Sales instance a_sale to invoke get_sale function
    a_single_sale = a_sale.get_sale(sales_id)
    if a_sale:
        return jsonify({"Product":a_single_sale}), 200
    return jsonify({"Message":"There is no sale record matching that ID"}), 404

#POST /sales endpoint
@app.route('/api/v1/sales', methods =['POST'])
def create_sale():
    #store the request data in user_input variable
    user_input = request.get_json(force=True)

    #validate user input
    attendant_name = user_input.get("attendant_name")
    if not attendant_name or attendant_name.isspace():
        return jsonify({"Message":"Attendant Name is required"}), 400

    no_of_pdts = user_input.get("no_of_products")
    if not no_of_pdts:
        return jsonify({"Message":"Number of products is required"}), 400
  
    ttl_profit = user_input.get("total_profit")
    if not ttl_profit:
        return jsonify({"Message":"Total profit is required"}), 400

    sale={
            "sales_id" : len(sales) + 1,
            "attendant_name" : attendant_name,
            "no_of_products": no_of_pdts,
            "total_profit": ttl_profit
    }
    
    #add the new sale record to the list of sales
    sales.append(sale)
    if sales:
        return jsonify({"Added Sale record": sale,"Message":"Sale record added successfully"}), 201
    else:
        return jsonify({"Message":"Insertion failed"}), 404

    