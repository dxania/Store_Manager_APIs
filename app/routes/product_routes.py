from flask import jsonify, flash, request, make_response

from app.exception_handler import InvalidUsage

from app import app

from app.models.product_models import Product

#instance of Products Class
product_object = Product()


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """Error handling and exception raising"""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/')
def index():
    """The first page and endpoint that 
    is rendered on loading the url
    """
    return """Products ==>
    <a href="https://store-manager-apis.herokuapp.com/api/v1/products">
    Navigate to this link to interact with the products endpoint</a><br><br>
    Sales ==>
    <a href="https://store-manager-apis.herokuapp.com/api/v1/sales">
    Navigate to this link to interact with the sales endpoint</a>
    """


@app.route('/api/v1/products', methods = ['GET'])
def get_products():
    """Retrieve all products function 
    wrapped around the Get /products endpoint
    """
    all_products = product_object.get_all_products()
    if all_products:
        return all_products, 200
    else:
        raise InvalidUsage('There are no products in the store', status_code=204) 
    

@app.route('/api/v1/products/<int:product_id>', methods = ['GET'])
def get_product(product_id):
    """Retrieve a particular product 
    function wrapped around the Get 
    /product/<int:product_id> endpoint
    """
    a_single_product = product_object.get_a_product(product_id)
    if a_single_product:
        return jsonify({"Product":a_single_product}), 200
    else:
        raise InvalidUsage('There is no product matching that ID', status_code=404)

@app.route('/api/v1/products', methods =['POST'])
def create_product():
    """Create a product function 
    wrapped around the Post /products 
    endpoint
    """
    #store the request data in user_input variable
    user_input = request.get_json(force=True)

    #validate user input
    pdt_name = user_input.get("product_name")
    if not pdt_name or pdt_name.isspace():
        raise InvalidUsage('Product Name is required', status_code=400)

    pdt_model = user_input.get("model_no")
    if not pdt_model or pdt_model.isspace():
        raise InvalidUsage('Product Quantity is required', status_code=400)

    pdt_category = user_input.get("product_category")
    if not pdt_category or pdt_category.isspace():
        raise InvalidUsage('Product Category is required', status_code=400)
    
    pdt_price = user_input.get("unit_price")
    if not pdt_price :
        raise InvalidUsage('Product Price is required', status_code=400)

    pdt_quantity = user_input.get("product_quantity")
    if not pdt_quantity:
        raise InvalidUsage('Product Quantity is required', status_code=400)

    #auto generate the product ID
    product_id = len(product_object.products) + 1
        
    #use the Products object to invoke the create_a_product function
    product = product_object.create_a_product(  product_id,
                                                pdt_name,pdt_model,
                                                pdt_category,pdt_price,
                                                pdt_quantity)

    #add the new product to the list of products
    product_object.products.append(product)
    if product_object.products:
        return product, 201
    else:
        raise InvalidUsage('Insertion failed', status_code=400)
