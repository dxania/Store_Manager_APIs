from flask import request, jsonify, Response

from app import app

from app.exception_handler import InvalidUsage

from app.models.sales_models import Sales

#instance of the Sales class
sales_object = Sales()


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """Error handling and exception raising"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

 
@app.route('/api/v1/sales', methods = ['GET'])
def get_sales():
    """Retrieve all sales function 
    wrapped around theGET /sales endpoint
    """
    #use Sales instance to call get_all_sales function
    all_sales = sales_object.get_all_sales()
    if all_sales:
        return jsonify({"Sale records": all_sales}), 200
    else:
        raise InvalidUsage('No sales have been added yet', status_code=404)


@app.route('/api/v1/sales/<int:sales_id>', methods = ['GET'])
def get_sale(sales_id):
    """Retrieve a particular sale record 
    function wrapped around the Get 
    /sales/<int:sales_id> endpoint
    """
    #use Sales instance to call get_sale function
    a_single_sale = sales_object.get_sale(sales_id)
    if a_single_sale:
        return jsonify({"Sale record":a_single_sale}), 200
    else:
        raise InvalidUsage('There is no sale record matching that ID', status_code=404)


@app.route('/api/v1/sales', methods =['POST'])
def create_sale():
    """Create a product function 
    wrapped around the Post /sales 
    endpoint
    """
    #store the request data in user_input variable
    user_input = request.get_json(force=True)

    #validate user input
    attendant_name = user_input.get("attendant_name")
    if not attendant_name or attendant_name.isspace():
        raise InvalidUsage('Attendant Name is required', status_code=400)

    no_of_pdts = user_input.get("no_of_products")
    if not no_of_pdts:
        raise InvalidUsage('Number of products is required', status_code=400)
  
    ttl_profit = user_input.get("total_profit")
    if not ttl_profit:
        raise InvalidUsage('Total profit is required', status_code=400)

    #auto generate the sales ID
    sales_id = len(sales_object.sales) + 1

    #use the Sales object to call the create_sale function
    sale = sales_object.create_sale(sales_id, attendant_name, 
                                    no_of_pdts, ttl_profit)

    #add the new sale record to the list of sales
    sales_object.sales.append(sale)
    if sales_object.sales:
        return sale, 201
    else:
        raise InvalidUsage('Insertion failed', status_code=400)

    